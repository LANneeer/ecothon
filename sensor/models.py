from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from sensor.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, editable=False)
    iin = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "iin"
    REQUIRED_FIELDS = ["phone"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.iin


class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    car_number = models.CharField(max_length=100)
    car_brand = models.CharField(max_length=100)
    car_ecology = models.ForeignKey("AirQuality", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return self.car_number


class AirQuality(models.Model):
    co_level = models.IntegerField()
    pm25_level = models.IntegerField()
    so_level = models.IntegerField()
    quality_status = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Air Quality"
        verbose_name_plural = "Air Qualities"

    def __str__(self):
        return f"<{self.pk} - {self.co_level} - {self.pm25_level} - {self.so_level} - {self.quality_status}>"
