from django.contrib import admin
from django.urls import path
from querysetapi1 import views

urlpatterns =[
    path('', views.home),
]