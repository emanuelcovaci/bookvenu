from django.shortcuts import render,render_to_response

# Create your views here.
def profile_detail(request):
    return render(request, 'profile/profile-details.html')
def change_password(request):
    return render(request, 'profile/profile-changepassword.html')
def history(request):
    return render(request, 'profile/profile-deals.html')