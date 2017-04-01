from django.shortcuts import render,render_to_response
from django.http import Http404
from django.contrib.auth.models import User
from forms import UserRegisterForm

# Create your views here.
def profile_detail(request):
        form = UserRegisterForm(data=request.POST or None)
        if request.method == 'POST':
            if form.is_valid() == True and acc_form.is_valid() == True:
                form.instance.set_password(form.cleaned_data['password'])
                form.save()
        return render(request, "profile/profile-details.html", {
            'form': form,
        })
def change_password(request):
    return render(request, 'profile/profile-changepassword.html')
def history(request):
    return render(request, 'profile/profile-deals.html')
def get_user_profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'profile/profile-details.html', {"user":user})