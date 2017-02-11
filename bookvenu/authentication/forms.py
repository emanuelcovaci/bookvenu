from django import forms


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
