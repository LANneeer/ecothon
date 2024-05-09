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
from sensor.views import home, about, contact, cto_registration, cto_login, tech_review, car_detail, loading, air_quality

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name='home'),
    path("about/", about, name='about'),
    path("contact/", contact, name='contact'),
    path("cto_registration/", cto_registration, name='cto_registration'),
    path("cto_login/", cto_login, name='cto_login'),
    path("tech_review/", tech_review, name='tech_review'),
    path("car_detail/<int:car_id>/", car_detail, name='car_detail'),
    path("loading/", loading, name='loading'),
    path("air_quality/", air_quality, name='air_quality'),


]
