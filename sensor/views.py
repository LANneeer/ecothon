from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

from sensor.forms import CarForm, UploadFileForm
from sensor.models import AirQuality
from .forms import CustomLoginForm, InspectionForm
from .forms import PhotoUploadForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def submit_car_info(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CarForm()
    return render(request, 'frame1.html', {'form': form})


def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])  # Assume this function processes the file.
            return redirect('success')
    else:
        form = UploadFileForm()
    return render(request, 'frame2.html', {'form': form})


def display_air_quality(request):
    data = AirQuality.objects.latest('id')
    return render(request, 'frame3.html', {'data': data})


def download_data(request):
    # Implement the logic to download data, perhaps as a CSV file.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    # Assume data_csv() generates CSV data.
    # response.write(data_csv())
    return response


def success(request):
    return render(request, 'frame4.html')


def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            service_code = form.cleaned_data.get('service_code')
            user = authenticate(username=username, password=password)
            if user is not None and user.profile.service_code == service_code:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid login details or service code')
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})


def start_inspection(request):
    if request.method == 'POST':
        form = InspectionForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save it or send it to another service)
            return redirect('inspection_success')  # Redirect to a new URL for success
    else:
        form = InspectionForm()
    return render(request, 'start_inspection.html', {'form': form})


def check_air_pollution(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = request.FILES['photo']
            fs = FileSystemStorage()
            filename = fs.save(photo.name, photo)
            uploaded_file_url = fs.url(filename)
            # Here you could add logic to analyze the photo for air pollution
            return redirect('results_page')  # assuming you redirect to a results page
    else:
        form = PhotoUploadForm()
    return render(request, 'check_air_pollution.html', {'form': form})
