from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import Car
from .models import CTO


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['owner', 'car_number', 'car_brand']
        widgets = {
            'owner': forms.TextInput(attrs={'class': 'form-control'}),
            'car_number': forms.TextInput(attrs={'class': 'form-control'}),
            'car_brand': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100, required=True)
    email = forms.EmailField(label='Email', required=True)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea, required=True)


class CTORegistrationForm(forms.Form):
    service_code = forms.CharField(label='Код услуги', max_length=100, required=True)
    password = forms.CharField(label='Пароль', max_length=100, required=True)
    confirm_password = forms.CharField(label='Подтвердите пароль', max_length=100, required=True)


class CTOLoginForm(forms.Form):
    service_code = forms.CharField(label='Код услуги', max_length=100, required=True)
    password = forms.CharField(label='Пароль', max_length=100, required=True)


class TechReviewForm(forms.Form):
    gov_number = forms.CharField(label='Гос. номер', max_length=100, required=True)
    tech_pass = forms.CharField(label='Тех. паспорт', max_length=100, required=True)


class UploadFileForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))


class CustomLoginForm(AuthenticationForm):
    service_code = forms.CharField(max_length=100, required=True)

    class Meta:
        fields = ['username', 'password', 'service_code']


class InspectionForm(forms.Form):
    registration_number = forms.CharField(label='Гос. регистрационный знак', max_length=100, required=True)
    document_number = forms.CharField(label='Номер техпаспорта', max_length=100, required=True)


class PhotoUploadForm(forms.Form):
    photo = forms.ImageField(label='Drop photo')


class CTOForm(forms.ModelForm):
    class Meta:
        model = CTO
        fields = ['password', 'service_code']
