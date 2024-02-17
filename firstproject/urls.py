"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from first_app import views



urlpatterns = [
    path('', views.begnn, name = 'begnn' ),
    path('admin/', admin.site.urls),
    path('first_app/', include('first_app.urls')),
    path('users', views.users, name = 'users' ),
    path('first_app/forms', views.form_name_view, name='form_name_view'),
    path('relative_temp', views.relative_temp, name='relaive_temp'),
    path('first_app/signup', views.signup_form, name='signup_form')
    
]
