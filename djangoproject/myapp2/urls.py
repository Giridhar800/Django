from django.urls import path
from myapp2 import views

urlpatterns = [
    path("my_view", views.my_view )
]