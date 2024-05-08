from django.contrib import admin
from sensor.models import Car, AirQuality, User

admin.site.register(User)
admin.site.register(Car)
admin.site.register(AirQuality)
