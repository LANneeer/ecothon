from django import forms

from users.models import Car


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


class UploadFileForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

class CustomLoginForm(forms.AuthenticationForm):
    service_code = forms.CharField(max_length=100, required=True)

    class Meta:
        fields = ['username', 'password', 'service_code']


class InspectionForm(forms.Form):
    registration_number = forms.CharField(label='Гос. регистрационный знак', max_length=100, required=True)
    document_number = forms.CharField(label='Номер техпаспорта', max_length=100, required=True)
    
class PhotoUploadForm(forms.Form):
    photo = forms.ImageField(label='Drop photo')