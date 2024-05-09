from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class AirQuality(models.Model):
    STATUSES = (
        ("OK", "Ok"),
        ("BAD", "Bad"),
    )
    co_level = models.IntegerField()
    pm25_level = models.IntegerField()
    so_level = models.IntegerField()
    quality_status = models.CharField(max_length=50, choices=STATUSES, default="OK")

    class Meta:
        verbose_name = "Air Quality"
        verbose_name_plural = "Air Qualities"

    def __str__(self):
        return f"<{self.pk} - {self.co_level} - {self.pm25_level} - {self.so_level} - {self.quality_status}>"
