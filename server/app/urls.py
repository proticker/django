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
    
]
