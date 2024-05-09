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
