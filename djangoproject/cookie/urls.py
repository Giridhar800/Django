from django.urls import path
from cookie import views

urlpatterns = [
    path('set', views.setcookie),
    path('get', views.getcookie),
]