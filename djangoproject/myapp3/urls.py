from django.urls import path
from myapp3 import views


urlpatterns = [
    path("", views.home),
    path("add", views.add),
]