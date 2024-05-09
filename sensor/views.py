from django.shortcuts import render, redirect

from sensor.models import AirQuality
from users.models import Car
from .forms import CTOForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
#========

def cto_registration(request):
    # serviceCode = request.POST.get('serviceCode', None)
    # password = request.POST.get('password', None)
    form = CTOForm(request.POST)
    if form.is_valid():
        form = form.save(commit=False)
    # return render(request, 'cto_registration.html')
    return redirect("cto_login")


def cto_login(request):
    return redirect("tech_review")


def tech_review(request):
    if request.method == "POST":
        try:
            tech_pass_post = request.POST.get('techPass', None)
            car = Car.objects.get(tech_pass=tech_pass_post)
            request.session["_metadata"] = tech_pass_post
        except Car.DoesNotExist:
            return redirect('/')
    # return render(request, 'logitech.html')
    # return redirect("car_detail", car_id=)


def car_detail(request):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        car = Car.objects.first()  # TODO: delete this line
    # return render(request, 'datatech.html', {'car': car})
    return redirect("air_quality")


def loading(request):
    return render(request, 'loading.html')


def air_quality(request):
    air_quality_data = AirQuality.objects.all()
    return render(request, 'showtech.html', {'data': air_quality_data})

