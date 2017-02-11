from django.shortcuts import render, redirect
from forms import LoginForm
from django.contrib.auth import logout, authenticate, login


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