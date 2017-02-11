from django.shortcuts import render, redirect
from forms import LoginForm
from django.contrib.auth import logout, authenticate, login


# Create your views here.

def login(request):
    if request.user.is_authenticated():
        return redirect('/')
    form = LoginForm(request.POST)
    errors = []
    if request.method == "POST":
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                errors.append("Email sau parola invalida")
    return render(request, 'authentication/login.html', {
        'errors': errors,
        'form': form
    })
