import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse
from .models import Project, Timesheet

@login_required
def dashboard(request):
    # --- DAY 9: SEARCH LOGIC ---
    # Get the search query from the URL (e.g., ?search=Portfolio)
    query = request.GET.get('search')
    
    if query:
        # Filter projects managed by user that match the name
        my_projects = Project.objects.filter(manager=request.user, name__icontains=query)
    else:
        my_projects = Project.objects.filter(manager=request.user)
    
    # Fetch the last 5 timesheets logged by this user
    recent_timesheets = Timesheet.objects.filter(employee=request.user).order_by('-created_at')[:5]
    
    context = {
        'projects': my_projects,
        'recent_timesheets': recent_timesheets,
        'search_query': query,
    }
    return render(request, 'projects/dashboard.html', context)

@login_required
def log_time(request):
    if request.method == "POST":
        project_id = request.POST.get('project')
        hours = request.POST.get('hours')
        date = request.POST.get('date')
        desc = request.POST.get('description')
        
        project = get_object_or_404(Project, id=project_id)
        
        Timesheet.objects.create(
            employee=request.user,
            project=project,
            hours_worked=hours,
            date=date,
            description=desc
        )
    return redirect('dashboard')

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    total_hours = Timesheet.objects.filter(project=project).aggregate(Sum('hours_worked'))['hours_worked__sum'] or 0
    
    # Day 7 Logic: Progress based on a 100h budget
    budget = 100 
    progress_percent = min((float(total_hours) / budget) * 100, 100)

    context = {
        'project': project,
        'total_hours': total_hours,
        'progress_percent': progress_percent,
        'budget': budget,
    }
    return render(request, 'projects/project_detail.html', context)

# --- NEW DAY 8: CSV EXPORT VIEW ---
@login_required
def export_timesheets_csv(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{project.name}_WorkLogs.csv"'

    writer = csv.writer(response)
    # Write Header Row
    writer.writerow(['Date', 'Employee', 'Hours Worked', 'Work Description'])

    # Write Data Rows from Database
    timesheets = Timesheet.objects.filter(project=project).order_by('-date')
    for ts in timesheets:
        writer.writerow([ts.date, ts.employee.username, ts.hours_worked, ts.description])

    return response