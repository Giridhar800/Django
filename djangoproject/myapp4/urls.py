from django.urls import path
from myapp4 import views

urlpatterns = [
    path("", views.index),
]

