from django.shortcuts import render, redirect

from sensor.infrastructure.strategy import car_brands_by_country, brand_to_country, get_eco_class, \
    get_emission_standards
from sensor.models import AirQuality
from users.models import Car, User, ServiceStation
from sensor import forms


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


# ========


def cto_registration(request):
    """
    CTO create account
    :param request:
    :return:
    """
    if request.method == "POST":
        service_code = request.POST.get('service_code', None)
        name = request.POST.get('name', None)
        address = request.POST.get('address', None)
        phone = request.POST.get('phone', None)
        password = request.POST.get('password', None)
        print(service_code, name, address, phone, password)
        user = User.objects.create_user(
            iin=service_code,
            phone=phone,
            password=password,
        )
        ServiceStation.objects.create(
            code=service_code,
            owner=user,
            name=name,
            address=address,
            phone=phone,
        )
        return redirect("cto_login")
    return render(request, 'cto_registration.html', {'form': forms.CTORegistrationForm})
    # return redirect("cto_login")


def cto_login(request):
    """
    CTO get and compare, if show error message
    :param request:
    :return:
    """
    if request.method == "POST":
        service_code = request.POST.get('service_code', None)
        password = request.POST.get('password', None)
        print(service_code, password)
        try:
            ServiceStation.objects.get(code=service_code)
            request.session["_metadata"] = service_code
        except ServiceStation.DoesNotExist:
            return render(request, 'cto_login.html', {'error': 'Service code or password is incorrect', "form": forms.CTOLoginForm})
        return redirect("tech_review")
    return render(request, 'cto_login.html', {'form': forms.CTOLoginForm, 'error': ""})


def tech_review(request):
    """
    Getting tech_pass and gov number to search in DB if exists or not
    :param request:
    :return:
    """
    if request.method == "POST":
        try:
            gov_number_post = request.POST.get('gov_number', None)
            tech_pass_post = request.POST.get('tech_pass', None)
            Car.objects.get(tech_pass=tech_pass_post)
            request.session["_metadata"] = tech_pass_post
        except Car.DoesNotExist:
            return render(request, 'logitech.html', {'error': 'Technical passport is incorrect', "form": forms.TechReviewForm})
        return redirect('car_detail')
    return render(request, 'logitech.html', {'error': '', 'form': forms.TechReviewForm})


def car_detail(request):
    """
    Show car details
    OK
    :param request:
    :return:
    """
    try:
        tech_pass_post = request.session["_metadata"]
        car = Car.objects.get(tech_pass=tech_pass_post)
    except Car.DoesNotExist:
        return render(request, 'logitech.html', {'error': 'Technical passport is incorrect', "form": forms.TechReviewForm})
    if request.method == "POST":
        brand = brand_to_country(car.car_brand, car_brands_by_country)
        eco_class = get_eco_class(car.date_of_release.year, brand)
        mq9 = 0.5
        mq135 = 0.3
        PM25 = 36
        data = get_emission_standards(mq9, mq135, PM25, eco_class)
        AirQuality.objects.create(
            co_level=data["eco_info"]["CO"],
            pm25_level=data["eco_info"]["PM25"],
            so_level=data["eco_info"]["NO"],
            quality_status=data["result"]
        )
        return redirect("air_quality")
    return render(request, 'datatech.html', {'car': car, 'form': forms.UploadFileForm})


def loading(request):
    return render(request, 'loading.html')


def air_quality(request):
    air_quality_data = AirQuality.objects.all().first()
    return render(request, 'showtech.html', {'data': air_quality_data})
