from django.urls import path
from editingview import views

urlpatterns = [
    path('view/', views.StudentModelView.as_view()),
    path('update/<int:pk>', views.StudentUpdateView.as_view()),
    path('del/<int:pk>', views.StudentDeleteView.as_view()),
    path('success/', views.SuccessTemplateView.as_view(), name='success'),
    path('nodel/', views.NoDeleteView.as_view(), name='nodelete'),
]
