"""
URL configuration for ecothon project.

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
from django.urls import path
from sensor.views import custom_login, start_inspection, check_air_pollution, home, about, contact

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name='home'),
    path("about/", home, name='about'),
    path("contact/", home, name='contact'),
    path("home/", home, name='home'),
    path('login/', custom_login, name='login'),
    path('inspection/', start_inspection, name='start_inspection'),
    path('check-air-pollution/', check_air_pollution, name='check_air_pollution'),
]
