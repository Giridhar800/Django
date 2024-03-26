from django.urls import path
from middle import views

urlpatterns = [
    path('', views.home_view),
]