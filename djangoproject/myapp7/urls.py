from django.urls import path
from myapp7 import views

urlpatterns = [
    path("", views.Mydetails),
]