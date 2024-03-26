"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("myapp/", include("myapp.urls")),
    path('myapp1/', include("myapp1.urls")),
    path('myapp3/', include("myapp3.urls")),
    path("myapp4/", include("myapp4.urls")),
    path("myapp5/", include("myapp5.urls")),
    path("myapp/", include("myapp6.urls")),
    path("myapp7/", include("myapp7.urls")),
    path("myapp8/", include("myapp8.urls")),
    path("myapp9/", include("myapp9.urls")),
    path("myapp10/", include("myapp10.urls")),
    path("myapp11/", include("myapp11.urls")),
    path('myapp12/', include('myapp12.urls')),
    path('cookie/', include('cookie.urls')),
    path('cookie1/', include('cookie1.urls')),
    path('cookie2/', include('cookie2.urls')),
    path('session/', include('session.urls')),
    path('persite/', include('persiteapp.urls')),
    path('perview/', include('perviewapp.urls')),
    path('signup/', include('signup.urls')),
    path('changepassword/', include('changepassword.urls')),
    path('generic/', include('genericview.urls')),
    path('edit/', include('editingview.urls')),
    path('pagination/', include('pagination.urls')),
    path('middleware/', include('middleware.urls')),
    path('middle/', include('middle.urls')),
    path('middleinheritance/', include('modelinheritance.urls')),
    path('query/', include('querysetapi.urls')),
    path('qapi1/', include('querysetapi1.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('reg/', include('registration.urls')),



]
