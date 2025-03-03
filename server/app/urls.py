from django.urls import path 
from .import views

urlpatterns = [
    path('test', views.test),  
    path('home', views.home),  
    path('index', views.index),  
    path('sample1', views.sample1),  
    path('sample2', views.sample2), 
    path('index2', views.index2), 
    path('add', views.add), 
    path('addcode', views.addcode),
    path('nums', views.nums), 
    path('maxNum', views.maxNum),
    path('number', views.number), 
    path('evenodd', views.evenodd),
    path('signup',views.signup),
    path('sign',views.sign),
    path("addStudent",views.add_student, name= "add_Student"),
    path('login/',views.login),
    path('login/log',views.log),
    path('login/signup',views.signup),
    path('login/logout',views.logout),
    path('logout/login',views.login),
    path('show',views.show),
    path('del/<int:id',views.dele),
    path('edit/ <int:id>',views.edit),
    path('encode/<int:id>',views.encode),

]
