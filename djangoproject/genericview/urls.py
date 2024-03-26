from django.urls import path
from genericview import views

urlpatterns = [
    path('student/', views.StudentListView.as_view(), name='studentlist'),
    path('student/<int:pk>', views.StudentDetailsView.as_view(), name='studentdetail'),
]