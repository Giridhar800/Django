from django.urls import path
from myapp5 import views
urlpatterns = [

    path("", views.date_time),
]
