from django.contrib import admin
from django.urls import path, include

from frontend import views

app_name= 'frontend'
urlpatterns = [
    path('', views.index,  name='index',),
    path('donate/', views.donate,  name='donate',),
    path('work/', views.work,  name='work',),
    path('team/', views.team,  name='team',),
    path('news/', views.index,  name='news',),
]
