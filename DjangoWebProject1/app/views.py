"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from . import models

def overview(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    class_all=models.AllTest.objects.all().values()
    print(class_all)
    class_testid=[int(i.get('ClassTest')) for i in list(class_all)]
    class_math=[int(i.get('Math2')) for i in list(class_all)]
    class_chinese=[int(i.get('Chinese2')) for i in list(class_all)]
    class_english=[int(i.get('English2')) for i in list(class_all)]
    class_phy=[int(i.get('Physics2')) for i in list(class_all)]
    class_bio=[int(i.get('Biology2')) for i in list(class_all)]
    class_che=[int(i.get('Chemistry2')) for i in list(class_all)]
    class_total=[int(i.get('total')) for i in list(class_all)]
    class_trend=int(((class_total[-1]-class_total[-2])/class_total[-2])*100)
    if class_trend>=0:
        class_trend='+'+str(class_trend)
    else:
        class_trend='-'+str(class_trend)
    print(class_trend)
    now_testid=max(class_testid)
    class_people=models.ClassGrade.objects.filter(TEST_id=3).count()
    next_test=31-datetime.now().day
    next_test_pre=((datetime.now().day)/31)*100
    final_test=(6%datetime.now().month)*30+(7-datetime.now().day)
    final_test_pre=((158-final_test)/158)*100
    print(class_people)
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
            'now_testid':now_testid,
            'next_testid':now_testid+1,
            'people':class_people,
            'trend':class_trend,
            'test_id':['第'+str(i)+'次考试' for i in class_testid],
            'math':class_math,
            'chinese':class_chinese,
            'english':class_english,
            'phy':class_phy,
            'bio':class_bio,
            'che':class_che,
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

def datas_search(request):
    """Renders the datas page."""
    assert isinstance(request, HttpRequest)
    q = request.GET.get('q')
    #判别语句
    if q=='20190440432':
        return render(
            request,
            'app/datas_search.html',
            {
                'title':'Datas',
                'message':'Database contrl page.',
                'year':datetime.now().year,
                'res':1,
                'typecode':'has-success',
                'searchmessage':'学号 '+q+' 搜索完成！'
            }
        )
    return render(
            request,
            'app/datas_search.html',
            {
                'title':'Datas',
                'message':'Database contrl page.',
                'year':datetime.now().year,
                'res':0,
                'typecode':'',
                'searchmessage':''
            }
        )

def datas_add(request):
    """Renders the predict page."""
    assert isinstance(request, HttpRequest)
    request.encoding='utf-8'
    res=''
    if request.method =="POST":
        studentid = request.POST['studentid']
        testid = request.POST['testid']
        sub1 = request.POST['sub1']
        sub2 = request.POST['sub2']
        sub3 = request.POST['sub3']
        sub4 = request.POST['sub4']
        sub5 = request.POST['sub5']
        sub6 = request.POST['sub6']
        if request.POST.get('name') and request.POST.get('classid'):
            name = request.POST['name']
            classid = request.POST['classid']
            res='学生'+name+'已成功入库！'
            #数据库代码1
        else:
            res='学生'+studentid+'已成功添加记录！'
            #数据库代码2
    return render(
        request,
        'app/datas_add.html',
        {
            'title':'Datas',
            'message':'Database contrl page.',
            'year':datetime.now().year,
            'res':res
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