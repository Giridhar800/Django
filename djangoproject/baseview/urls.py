from django.urls import path
from baseview import views

urlpatterns = [
    path('fun/', views.fun_view, {'template_name': 'home.html'}),
    path('fun1/', views.fun_view, {'template_name': 'home1.html'}),
    path('cls/', views.class_view.as_view(template_name='home.html')),
    path('cls1/', views.class_view.as_view(template_name='home1.html')),
    path('home/', views.MyTemplateView.as_view(extra_context={'age': 24})),
    path('f/', views.flipkart.as_view()),
]