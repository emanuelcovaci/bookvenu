from django.shortcuts import render,render_to_response
from django.http import Http404
from django.contrib.auth.models import User

# Create your views here.
def profile_detail(request):
    return render(request, 'profile/profile-details.html')
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