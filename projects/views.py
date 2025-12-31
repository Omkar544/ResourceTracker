from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # THIS WAS MISSING
from .models import Project, Timesheet

@login_required
def dashboard(request):
    # Fetch projects where the logged-in user is the manager
    my_projects = Project.objects.filter(manager=request.user)
    
    # Fetch the last 5 timesheets logged by this user
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
        
        # Get the actual Project object
        project = Project.objects.get(id=project_id)
        
        # Create the new entry linked to dev_54
        Timesheet.objects.create(
            employee=request.user,
            project=project,
            hours_worked=hours,
            date=date,
            description=desc
        )
    return redirect('dashboard')