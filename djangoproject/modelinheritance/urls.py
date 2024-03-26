from django.contrib import admin
from django.urls import path
from modelinheritance import views

urlpatterns = [
    path('', views.display)
]