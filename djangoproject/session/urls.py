from django.urls import path
from session import views

urlpatterns = [
    path("", views.page_count_view),

]