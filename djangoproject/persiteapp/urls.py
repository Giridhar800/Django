from django.urls import path
from persiteapp import views

urlpatterns = [
    path('', views.v1),
]
