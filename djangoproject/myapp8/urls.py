from django.urls import path
from myapp8 import views

urlpatterns = [
    path("", views.Studentview)
]