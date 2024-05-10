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
    service_code = forms.CharField(label='CTO code', max_length=100, required=True)
    name = forms.CharField(label='name', max_length=100, required=False)
    address = forms.CharField(label='address', max_length=100, required=True)
    phone = forms.CharField(label='phone', max_length=100, required=True)
    password = forms.CharField(label='password', max_length=100, required=True, widget=forms.PasswordInput())


class CTOLoginForm(forms.Form):
    service_code = forms.CharField(label='CTO code', max_length=100, required=True)
    password = forms.CharField(label='password', max_length=100, required=True, widget=forms.PasswordInput())


class TechReviewForm(forms.Form):
    gov_number = forms.CharField(label='government number', max_length=100, required=True)
    tech_pass = forms.CharField(label='tech passport', max_length=100, required=True)


class UploadFileForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))


class CustomLoginForm(AuthenticationForm):
    service_code = forms.CharField(max_length=100, required=True)

    class Meta:
        fields = ['username', 'password', 'service_code']


class InspectionForm(forms.Form):
    registration_number = forms.CharField(label='Government registration number', max_length=100, required=True)
    document_number = forms.CharField(label='tech passport', max_length=100, required=True)


class PhotoUploadForm(forms.Form):
    photo = forms.ImageField(label='Drop photo', required=True, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))


class CTOForm(forms.ModelForm):
    class Meta:
        model = CTO
        fields = ['password', 'service_code']
