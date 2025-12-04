from django.shortcuts import render
from django.http import HttpResponse

# Test view to ensure the base template and settings are working
def test_config_view(request):
    """Renders the base template to confirm Tailwind/Templates are linked."""
    context = {
        'test_message': 'Tailwind CSS and Template Inheritance are correctly configured!',
    }
    # Renders the base.html file
    return render(request, 'base.html', context)