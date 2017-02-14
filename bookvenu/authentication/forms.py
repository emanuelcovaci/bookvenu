from django.core.validators import validate_email
from django.contrib.auth.models import User
from django import forms
from .models import Account

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
class UserCustomForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
                                'placeholder': 'Retype password',
                                'label': 'Retype password',
                                'required': 'required'}))
    class Meta:
        model = User
        fields = ['username','email','password']
        widgets = {
                'username' : forms.TextInput({'required' : 'required',
                                                'placeholder': 'Username'}),

                'email' : forms.EmailInput({'required' : 'required',
                                                'placeholder': 'E-mail'}),
                'password' : forms.PasswordInput({'required' : 'required',
                                                'placeholder': 'Type Password'})
            }
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username = username).count():
            raise forms.ValidationError("Username already exists")
        elif len(username)<8:
            raise forms.ValidationError("Username is too short")
        elif (
             not (user_name.isalnum())
            ):
            raise forms.ValidationError("Username contains invalid characters")
        else:
            return username



    def clean_email(self):
        email = self.cleaned_data['email']
        if validate_email(email):
            raise forms.ValidationError("Email is not valid")
        elif User.objects.filter(email=email):
            raise forms.ValidationError("This email already exists")
        return email


    def clean_password(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError("Passwords do not match")
        elif password.isdigit():
            raise forms.ValidationError("Password is entirely numeric")
        elif password.isalpha():
            raise forms.ValidationError("Password does not have any digits")
        elif len(password)<8:
            raise forms.ValidationError("Password is too short")
        if len(password) > 16:
            raise forms.ValidationError("Password is too long")
        else:
            return password

class AccountRegistrationForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['phonenumber','birthday']
        widgets = {
            'phonenumber' :  forms.TextInput({'required' : 'required'})
        }

    def clean_phonenumber(self):
        phonenumber = self.cleaned_data['phonenumber']
        if phonenumber.isdigit() == False or len(phonenumber) != 10 or phonenumber[0] != '0' or phonenumber[1] != '7':
            raise forms.ValidationError("Phone number is not valid")
        else:
            return phonenumber