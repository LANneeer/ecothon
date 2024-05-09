from django.shortcuts import render

from sensor.models import AirQuality
from users.models import Car


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
#========

def cto_registration(request):
    return render(request, 'cto_registration.html')


def cto_login(request):
    return render(request, 'cto_login.html')


def tech_review(request):
    return render(request, 'logitech.html')


def car_detail(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        car = Car.objects.first()  # TODO: delete this line
    return render(request, 'datatech.html', {'car': car})


def loading(request):
    return render(request, 'loading.html')


def air_quality(request):
    air_quality_data = AirQuality.objects.all()
    return render(request, 'showtech.html', {'data': air_quality_data})

