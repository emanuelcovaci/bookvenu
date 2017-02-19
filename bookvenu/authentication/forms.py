from django.core.validators import validate_email
from django.contrib.auth.models import User
from django import forms
from .models import Account
from captcha.fields import ReCaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label="Username",
                          widget=forms.TextInput(attrs={
                              'required': 'required',
                              'placeholder': 'Username'
                          }))

    password = forms.CharField(max_length=100, label="Password",
                          widget=forms.PasswordInput(attrs={
                              'required': 'required',
                              'placeholder': 'Password'
                          }))

class UserRegisterForm(forms.ModelForm):
    recaptcha = ReCaptchaField()
    retypepassword = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Retype password',
        'label': 'Retype password',
        'required': 'required'}))

    class Meta:
        model = User
        fields = ['username', 'email',  'password']
        widgets = {
            'username': forms.TextInput({'required': 'required',
                                         'placeholder': 'Username'}),
            'email': forms.EmailInput({'required': 'required',
                                       'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'required': 'required',
                                                   'placeholder': 'Password'})
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if validate_email(email):
            raise forms.ValidationError("Email is not valid")
        elif User.objects.filter(email=email):
            raise forms.ValidationError("This email already exists")
        return email

    def clean_username(self):
        user_name = self.cleaned_data['username']
        if User.objects.filter(username=user_name).count():
            raise forms.ValidationError("This username already exists")
        elif (
                not (user_name.isalnum() or user_name.isalpha())
        ):
            raise forms.ValidationError("Username contains invalid characters")
        return user_name

    def clean_retypepassword(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['retypepassword']
        if password.isdigit():
            raise forms.ValidationError("Password is entirely numeric")
        if password != password2:
            raise forms.ValidationError("Passwords do not match")
        if len(password) < 8:
            raise forms.ValidationError("Password is too short")
        return password2
