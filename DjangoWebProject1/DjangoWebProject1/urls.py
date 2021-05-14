"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.overview, name='home'),
    path('dataschange/', views.datas_change, name='dataschange'),
    path('datasearch/', views.datas_search, name='datasearch'),
    path('subjectpredict/', views.subject_predict, name='subjectpredict'),
    path('classpredict/', views.class_predict, name='classpredict'),
    path('classanalysis/', views.class_analysis, name='classanalysis'),
    path('subjectanalysis/', views.subject_analysis, name='subjectanalysis'),
    path('datasadd/', views.datas_add, name='datasadd'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
handler400 = views.bad_request
handler403 = views.permission_denied
handler404 = views.page_not_found
handler500 = views.page_error