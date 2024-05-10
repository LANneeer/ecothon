from django.shortcuts import render, redirect

from sensor.infrastructure.strategy import car_brands_by_country, brand_to_country, get_eco_class, \
    get_emission_standards
from sensor.models import AirQuality
from users.models import Car
from sensor import forms


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


# ========


def cto_registration(request):
    # serviceCode = request.POST.get('serviceCode', None)
    # password = request.POST.get('password', None)
    if request.method == "POST":
        form = forms.CTOForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
        return redirect("cto_login")
    return render(request, 'cto_registration.html', {'form': forms.CTOForm})
    # return redirect("cto_login")


def cto_login(request):
    if request.method == "POST":
        print(request.POST)

        form = forms.CTOForm(request.POST)
        print(form.data.items())
        print(request)
        # try:
        #     service_code_post = request.POST.get('serviceCode', None)
        #     password_post = request.POST.get('password', None)
        #     cto = CTO.objects.get(service_code=service_code_post, password=password_post)
        #     request.session["_metadata"] = service_code_post
        # except CTO.DoesNotExist:
        #     return redirect('/')
        return redirect("tech_review")
    return render(request, 'cto_login.html', {'form': forms.CTOLoginForm})


def tech_review(request):
    if request.method == "POST":
        # try:
        #     print(request.POST)
        #     tech_pass_post = request.POST.get('techPass', None)
        #     print(tech_pass_post)
        #     car = Car.objects.get(tech_pass=tech_pass_post)
        #     print(car)
        #     request.session["_metadata"] = tech_pass_post
        # except Car.DoesNotExist:
        #     return redirect('tech_review')
        return redirect('car_detail')
    return render(request, 'logitech.html', {'form': forms.TechReviewForm})


def car_detail(request):
    if request.method == "POST":
        tech_pass_post = request.POST.get('techPass', None)
        car = Car.objects.all().first()
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
    try:
        # car_id = request.session["_metadata"]
        car = Car.objects.all().first()
    except Car.DoesNotExist:
        car = Car.objects.first()  # TODO: delete this line
    return render(request, 'datatech.html', {'car': car, 'form': forms.UploadFileForm})


def loading(request):
    return render(request, 'loading.html')


def air_quality(request):
    air_quality_data = AirQuality.objects.all().first()
    return render(request, 'showtech.html', {'data': air_quality_data})
