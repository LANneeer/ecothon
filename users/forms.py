from django import forms


class RegistrationForm(forms.Form):
    service_code = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    service_code = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class Logitech(forms.Form):
    gov_reg_sign = forms.CharField()
    tech_pass = forms.CharField()
