from django.urls import path
from myapp9 import views

urlpatterns = [
    path("", views.studentviewinput)
]