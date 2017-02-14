from django.shortcuts import render, redirect
from forms import LoginForm,UserCustomForm,AccountRegistrationForm
from django.contrib.auth import logout, authenticate, login

from .models import Account
# Create your views here.

def login_view(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        errors = []
        form = LoginForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('/')

                else:
                    errors.append('Incorrect username or password')

            else:
                errors.append('Invalid form')
        return render(request, "authentication/login.html", {
            'form': form,
            'errors': errors})


def logout_view(request):
    logout(request)
    return redirect('/')

def register_page(request):
    form = UserCustomForm(data=request.POST or None)
    acc_form = AccountRegistrationForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid() and acc_form.is_valid():
            form.instance.set_password(form.cleaned_data['password'])
            form.save()
            acc_form.instance.user = form.instance
            acc_form.save()
            user = authenticate(username=form.instance.username,
                                password=form.cleaned_data['password'])
            login(request, user)
            return redirect('/')
    return render(request, "authentication/register.html", {
        'form': form,
        'acc_form': acc_form
    })