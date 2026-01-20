import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse
from .models import Project, Timesheet

# --- DAY 1 & 6: CORE DASHBOARD LOGIC ---
# This view was initialized on Day 1 and fully functional by Day 6.
# It handles project filtering and recent activity display.
@login_required
def dashboard(request):
    # Day 9: Integrated Search logic to filter projects by name
    query = request.GET.get('search')
    
    if query:
        # Uses icontains for case-insensitive partial matches
        my_projects = Project.objects.filter(manager=request.user, name__icontains=query)
    else:
        # Standard view: shows projects where the logged-in user is the manager
        my_projects = Project.objects.filter(manager=request.user)
    
    # Day 6: Fetching the 5 most recent timesheets for the activity feed
    recent_timesheets = Timesheet.objects.filter(employee=request.user).order_by('-created_at')[:5]
    
    context = {
        'projects': my_projects,
        'recent_timesheets': recent_timesheets,
        'search_query': query,
    }
    return render(request, 'projects/dashboard.html', context)

# --- DAY 6: INTERACTIVE DATA ENTRY ---
# Handles POST requests from the dashboard to log work hours.
@login_required
def log_time(request):
    if request.method == "POST":
        project_id = request.POST.get('project')
        hours = request.POST.get('hours')
        date = request.POST.get('date')
        desc = request.POST.get('description')
        
        project = get_object_or_404(Project, id=project_id)
        
        # Saves the entry linked to the current logged-in user (dev_54)
        Timesheet.objects.create(
            employee=request.user,
            project=project,
            hours_worked=hours,
            date=date,
            description=desc
        )
    return redirect('dashboard')

# --- DAY 7 & 11: ANALYTICS & FINANCIALS ---
# Expanded on Day 11 to include budget and cost calculations.
@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    # Day 7: Using Django Aggregation to sum all hours for this project
    total_hours = Timesheet.objects.filter(project=project).aggregate(Sum('hours_worked'))['hours_worked__sum'] or 0
    
    # Day 11: Financial tracking - Calculating total cost based on hourly rate
    hourly_rate = getattr(project, 'hourly_rate', 50.00) 
    total_cost = float(total_hours) * float(hourly_rate)
    
    # Day 7: Progress logic (assuming a standard 100h project budget)
    budget = 100 
    progress_percent = min((float(total_hours) / budget) * 100, 100)

    context = {
        'project': project,
        'total_hours': total_hours,
        'total_cost': total_cost,
        'progress_percent': progress_percent,
        'budget': budget,
    }
    return render(request, 'projects/project_detail.html', context)

# --- DAY 8: DATA PORTABILITY ---
# Generates a downloadable CSV for billing and reporting.
@login_required
def export_timesheets_csv(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    # Setting the response type to CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{project.name}_WorkLogs.csv"'

    writer = csv.writer(response)
    # Writing the header row
    writer.writerow(['Date', 'Employee', 'Hours Worked', 'Work Description'])

    # Querying timesheets specifically for this project
    timesheets = Timesheet.objects.filter(project=project).order_by('-date')
    for ts in timesheets:
        writer.writerow([ts.date, ts.employee.username, ts.hours_worked, ts.description])

    return response

# --- DAY 10: USER MANAGEMENT ---
# Displays professional details from the Custom User Model created on Day 3.
@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {
        'employee': request.user
    })