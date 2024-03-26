from django.urls import path
from pagination import views

urlpatterns = [

        path('all/', views.PageListView.as_view()),
        path('detail/<int:pk>', views.PageDetailView.as_view(),name='page'),
  ]