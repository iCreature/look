"""
Definition of urls for DjangoWebProject5.
"""
from datetime import datetime
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('Write/<str:test>', views.Write, name='exam'),
    path('about/', views.about, name='about'),
    path('studentDash/',views.sDash, name ='s_Dash'),
    path('adminDash/',views.aDash,name ='a_Dash'),
    path('S_set/',views.SetS,name='SetS'),
    path('A_set/',views.SetA,name='SetA'),
    path('testInfo/',views.T_Info,name='test_info'),
    path('testCreate/',views.T_Create, name='test_create'),
    path('AddUser/',views.Add, name='adduser'),
    path('Option/',views.OptionAdd, name='opt'),
    path('Add/',views.addstudent, name ='add'),
    path('menu',views.menu,name ='menu_'),
    path('success',views.success,name='success'),
    path('view',views._view,name='list'),
    path('testList',views.testList,name='test'),
    path('F_student',views._forgetStudent, name='resetS'),
    path('F_admin',views._forgetAdmin,name='resetA'),
    #path('adminDash/'),
    path('student',views.studentView,name='studentV'),
    path('writing/',views.current,name='currentV'),
    path('Schedule/',views.dule,name='spdf'),
    path('upload/',views.upload,name='upload'),
    path('submitted',views.submit,name='sub'),
    path('schedule',views.schedule,name='scheduleV'),
    #path('download/',views.PdfExams.as_view('/schedulepdf.html'),name='sPdf'),
    path('loginAdmin',views.login_admin,name='adminLogin'),
    path('Exam/upload/',views.upload_pdf,name='upload_exam'),
    path('login',views.login_student,name='login'),
    path('Exam/',views.upload_list,name='upload_list'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls), 
]#+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
