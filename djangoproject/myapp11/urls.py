from django.urls import path
from myapp11 import views

urlpatterns = [
    path("", views.studentinputview),
]