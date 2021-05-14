"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from . import models

#总览页面
def overview(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    #获取所有班级的所有次考试，得到最近考试次数
    class_all_full_prime=models.AllTest.objects.all().values()
    class_testid=[int(i.get('TesT_id')) for i in list(class_all_full_prime)]
    now_testid=max(class_testid)

    #获得当前班级的所有次数考试，将其打包为各学科值
    class_all_full=models.AllTest.objects.filter(Class='4').values()
    class_all=list(class_all_full)
    test_id,math,english,chinese,phy,bio,che=[],[],[],[],[],[],[]
    for i in class_all:
        test_id.append('第'+str(i.get('TesT_id'))+'次考试')
        math.append(i.get('Math2'))
        english.append(i.get('English2'))
        chinese.append(i.get('Chinese2'))
        phy.append(i.get('Physics2'))
        bio.append(i.get('Biology2'))
        che.append(i.get('Chemistry2'))

    #print(test_id,math,english,chinese,phy,bio,che)
    
    #获得第选定班级，最近一次考试的所有成绩
    grade_all=models.ClassGrade.objects.filter(TEST_id=now_testid,CLASS='4').values()
    grade=list(grade_all)

    #获取趋势并计算
    class_total=[int(i.get('total')) for i in list(class_all)]
    class_trend=int(((class_total[-1]-class_total[-2])/class_total[-2])*100)
    if class_trend>=0:
        class_trend='+'+str(class_trend)
    else:
        class_trend='-'+str(class_trend)

    #获取顺位并处理
    class_rank= class_all_full_prime.filter(TesT_id=now_testid).order_by('total')
    temp=0
    for i in class_rank:
        temp+=1
        if i.get('Class')=='4':
            rank=temp
        else:
            rank='error'
            temp=0
    #获取班级人数
    class_people=models.ClassGrade.objects.filter(TEST_id=now_testid,CLASS='4').count()
    #高考天数与月考天数
    next_test=31-datetime.now().day
    next_test_pre=((datetime.now().day)/31)*100
    final_test=(6%datetime.now().month)*30+(7-datetime.now().day)
    final_test_pre=((158-final_test)/158)*100
    return render(
        request,
        'app/index.html',
        {
            'title':'总览/Overview',
            'year':datetime.now().year,
            'next_test':next_test,
            'next_test_precent':int(next_test_pre),
            'final_test':final_test,
            'final_test_precent':int(final_test_pre),
            'now_testid':now_testid,
            'next_testid':now_testid+1,
            'people':class_people,
            'trend':class_trend,
            'grade':grade[:8],
            'testid':test_id,
            'math':math,
            'chinese':chinese,
            'english':english,
            'phy':phy,
            'bio':bio,
            'che':che,
            'rank':rank,
        }
    )

def datas_change(request):
    """Renders the datas page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/datas_change.html',
        {
            'title':'数据修改/Datas',
            'message':'database contrl page.',
            'year':datetime.now().year,
        }
    )

def datas_search(request):
    """Renders the datas page."""
    assert isinstance(request, HttpRequest)
    #使用GET方法从前端获取搜索学号
    q = request.GET.get('q')
    #判别语句
    search_res=models.ClassGrade.objects.filter(studentNum=q).order_by('TEST_id')
    #如果存在
    if search_res:
        search_grade=list(search_res.values())
        search_name=search_grade[0].get('STName')
        test_id,math,english,chinese,phy,bio,che,total=[],[],[],[],[],[],[],[]
        for i in search_grade:
            test_id.append('第'+str(i.get('TEST_id'))+'次考试')
            math.append(i.get('Math3'))
            english.append(i.get('English3'))
            chinese.append(i.get('Chinese3'))
            phy.append(i.get('Physics3'))
            bio.append(i.get('Biology3'))
            che.append(i.get('Chemistry3'))
            total.append(i.get('Total'))
        return render(
            request,
            'app/datas_search.html',
            {
                'title':'数据查询/Datas',
                'message':'Database contrl page.',
                'year':datetime.now().year,
                'res':1,
                'typecode':'has-success',
                'searchmessage':'学号 '+q+' 搜索完成！',
                'search_res':search_res,
                'testid':test_id,
                'math':math,
                'chinese':chinese,
                'english':english,
                'phy':phy,
                'bio':bio,
                'che':che,
                'total':total,
                'name':search_name,
            }
        )
    return render(
            request,
            'app/datas_search.html',
            {
                'title':'数据查询/Datas',
                'message':'Database contrl page.',
                'year':datetime.now().year,
                'res':0,
                'typecode':'',
                'searchmessage':'',
                'search_res':'',
                'testid':'',
                'math':'',
                'chinese':'',
                'english':'',
                'phy':'',
                'bio':'',
                'che':'',
                'total':'',
                'name':'',
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
            'title':'数据提交/Datas',
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
            'title':'成绩预测/Predict',
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
            'title':'单科预测/Predict',
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
            'title':'班级分析/Analysis',
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
            'title':'学况速览/Analysis',
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