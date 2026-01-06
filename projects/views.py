from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum  # Required for Day 7 analytics
from .models import Project, Timesheet

@login_required
def dashboard(request):
    my_projects = Project.objects.filter(manager=request.user)
    recent_timesheets = Timesheet.objects.filter(employee=request.user).order_by('-created_at')[:5]
    
    context = {
        'projects': my_projects,
        'recent_timesheets': recent_timesheets,
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

# --- NEW DAY 7 VIEW ---
@login_required
def project_detail(request, pk):
    # Fetch the project or return 404 if not found
    project = get_object_or_404(Project, pk=pk)
    
    # Logic: Sum all hours worked on this specific project
    total_hours = Timesheet.objects.filter(project=project).aggregate(Sum('hours_worked'))['hours_worked__sum'] or 0
    
    # Logic: Calculate progress percentage (Assuming a 100-hour budget for demo)
    budget = 100 
    progress_percent = min((float(total_hours) / budget) * 100, 100)

    context = {
        'project': project,
        'total_hours': total_hours,
        'progress_percent': progress_percent,
        'budget': budget,
    }
    return render(request, 'projects/project_detail.html', context)