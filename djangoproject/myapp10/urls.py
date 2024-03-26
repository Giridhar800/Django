from django.urls import path
from myapp10 import views

urlpatterns = [
    path("", views.studentinputview),
]