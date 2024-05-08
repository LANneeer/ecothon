from django.http import HttpResponse
from django.shortcuts import render, redirect

from sensor.forms import CarForm, UploadFileForm
from sensor.models import AirQuality


def home(request):
    return render(request, 'base.html')


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
