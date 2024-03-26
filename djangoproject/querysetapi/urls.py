from django.contrib import admin
from django.urls import path
from querysetapi import views

urlpatterns =[
    path('', views.v1),
]