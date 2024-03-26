from django.urls import path
from cookie2 import views

urlpatterns = [
    path('count', views.count_view),

]