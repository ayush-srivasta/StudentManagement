from django.urls import path
from django.urls.conf import include
from .import views
urlpatterns = [
path('',views.loginPage,name='login'),
path('signup/',views.signup,name='signup'),
path('main/',views.main,name='main'),
path('home/',views.home,name='home'),
path('verify/',views.verify,name='verify'),
path('logout/',views.Logout,name='logout'),
path('subject/<str:str>',views.subject,name='subject'),
path('stuList/<str:str>',views.stuList,name='stuList'),
path('subjectTeacher/<str:str>/<str:subject>',views.subjectTeacher,name='subjectTeacher')

]
