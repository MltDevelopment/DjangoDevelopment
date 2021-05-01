"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def page_not_found(request,exception,template_name='error/404.html'):
    
    return render(request,template_name)

def page_error(request,template_name='error/500.html'):
    #404
    return render(request,template_name)

def permission_denied(request,exception,template_name='error/403.html'):
    #403
    return render(request, template_name)

def bad_request(request,exception,template_name='error/400.html'):
    #400
    return render(request, temptale_name)