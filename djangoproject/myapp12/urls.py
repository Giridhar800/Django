from django.contrib import admin
from django.urls import path
from myapp12 import views


urlpatterns = [
    path('', views.msg),
    ]