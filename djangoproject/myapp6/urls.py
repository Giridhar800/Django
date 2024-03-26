from django.urls import path
from myapp6 import views

urlpatterns = [
    path("", views.displayemp),

]
