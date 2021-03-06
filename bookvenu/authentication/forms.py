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

    retypepassword = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Retype password',
        'label': 'Retype password',
        'required': 'required'}))

    class Meta:
        model = User
        fields = ['username', 'email',  'password' , 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput({'required': 'required',
                                         'placeholder': 'Username'}),
            'email': forms.EmailInput({'required': 'required',
                                       'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'required': 'required',
                                                   'placeholder': 'Password'}),
            'first_name': forms.TextInput({'required': 'required',
                                         'placeholder': 'First Name'}),
            'last_name': forms.TextInput({'required': 'required',
                                         'placeholder': 'Last Name'}),
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


    def clean_firstname(self):
        first_name = self.cleaned_data['firstname']
        if (
                not (first_name.isalnum() or first_name.isalpha())
        ):
            raise forms.ValidationError("Name contains invalid characters")
        return first_name


    def clean_lastname(self):
        last_name = self.cleaned_data['lastname']
        if (
                not (last_name.isalnum() or last_name.isalpha())
        ):
            raise forms.ValidationError("Name contains invalid characters")
        return last_name


class AccRegisterForm(forms.ModelForm):
    recaptcha = ReCaptchaField()
    class Meta:
        model = Account
        fields = ['phonenumber','city','country']
        widgets = {
            'phonenumber' : forms.TextInput({'required':'required','placeholder':'Phonenumber'}),
            'city' : forms.TextInput({'required':'required','placeholder':'City'}),
            'country' : forms.TextInput({'required':'required','placeholder':'Country'}),
        }
    def clean_phonenumber(self):
        phone_number = self.cleaned_data['phonenumber']
        if phone_number[0] != '0' or phone_number[1] != '7' or len(phone_number) != 10 or phone_number.isdigit() == False:
            raise forms.ValidationError("Invalid phonenumber")
        return phone_number

    def clean_city(self):
        city = self.cleaned_data['city']
        if city.isalpha == False:
            raise forms.ValidationError("City name contains invalid characters")
        return city

    def clean_country(self):
        country = self.cleaned_data['country']
        if country.isalpha == False:
            raise forms.ValidationError("Country name contains invalid characters")
        return country

class ChangePass(forms.Form):
    oldpassword = forms.CharField(max_length=20, min_length=8,
                                 label="Old password",
                                 widget=forms.PasswordInput(
                                     attrs={'required': 'required'}))
    password = forms.CharField(max_length=20, min_length=8,
                                 label="New password",
                                 widget=forms.PasswordInput(
                                     attrs={'required': 'required'}))
    retypepassword = forms.CharField(max_length=20, min_length=8,
                                 label="Type again the new password",
                                 widget=forms.PasswordInput(
                                     attrs={'required': 'required'}))
    def clean_retypepassword(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('retypepassword')
        if password.isdigit():
            raise forms.ValidationError("Password is entirely numeric")
        if password != password2:
            raise forms.ValidationError("Passwords do not match")
        if len(password) < 8:
            raise forms.ValidationError("Password is too short")
        return password2




