"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def overview(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    next_test=3
    next_test_pre=((30-3)/30)*100
    final_test=130
    final_test_pre=((365-130)/365)*100
    return render(
        request,
        'app/index.html',
        {
            'title':'Overview',
            'year':datetime.now().year,
            'next_test':next_test,
            'next_test_precent':int(next_test_pre),
            'final_test':final_test,
            'final_test_precent':int(final_test_pre),
        }
    )

def datas_change(request):
    """Renders the datas page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/datas_change.html',
        {
            'title':'Datas',
            'message':'database contrl page.',
            'year':datetime.now().year,
        }
    )

def datas_serach(request):
    """Renders the datas page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/datas_serach.html',
        {
            'title':'Datas',
            'message':'database contrl page.',
            'year':datetime.now().year,
        }
    )

def class_predict(request):
    """Renders the predict page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/class_predict.html',
        {
            'title':'Predict',
            'message':'Predict page.',
            'year':datetime.now().year,
        }
    )

def subject_predict(request):
    """Renders the predict page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/subject_predict.html',
        {
            'title':'Predict',
            'message':'Predict page.',
            'year':datetime.now().year,
        }
    )
def class_analysis(request):
    """Renders the analysis page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/class_analysis.html',
        {
            'title':'Analysis',
            'message':'Analysis page.',
            'year':datetime.now().year,
        }
    )
def subject_analysis(request):
    """Renders the analysis page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/subject_analysis.html',
        {
            'title':'Analysis',
            'message':'Analysis page.',
            'year':datetime.now().year,
        }
    )
def detail_analysis(request):
    """Renders the analysis page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/detail_analysis.html',
        {
            'title':'Analysis',
            'message':'Analysis page.',
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