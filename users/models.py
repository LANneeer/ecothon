import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from sensor.models import AirQuality
from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, auto_created=True, default=uuid.uuid4)
    iin = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
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
    gov_reg_sign = models.CharField(max_length=100, unique=True, verbose_name="Government registration sign")
    tech_pass = models.CharField(max_length=100, unique=True, verbose_name="Technical passport")
    date_of_release = models.DateField(verbose_name="Date of release")
    serial_number = models.CharField(max_length=100, unique=True, verbose_name="Serial number")
    body_number = models.CharField(max_length=100, unique=True, verbose_name="Body number")
    frame_number = models.CharField(max_length=100, unique=True, verbose_name="Frame number")
    engine_number = models.CharField(max_length=100, unique=True, verbose_name="Engine number")
    car_category = models.CharField(max_length=100, verbose_name="Car category")
    gas_cylinder_number = models.CharField(max_length=100, verbose_name="Gas cylinder number")
    car_number = models.CharField(max_length=100, unique=True, verbose_name="Car number")
    car_brand = models.CharField(max_length=100, verbose_name="Car brand")
    car_ecology = models.ForeignKey(AirQuality, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return self.car_number


class ServiceStation(models.Model):
    code = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="service_stations")
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Service Station"
        verbose_name_plural = "Service Stations"

    def __str__(self):
        return self.code
