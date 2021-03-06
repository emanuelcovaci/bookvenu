from django.shortcuts import render, redirect
from forms import Edit_profile, Edit_profile2
from django.contrib.auth.decorators import login_required
from post.models import EventModel,Reserve

# Create your views here.
@login_required
def profile_detail(request):
    current_user = request.user
    user_form = Edit_profile(data=request.POST or None,instance=current_user,user=current_user)
    account_form = Edit_profile2(data=request.POST or None,instance=current_user.account)
    if request.method == 'POST':
        if user_form.is_valid() and account_form.is_valid():
            user_form.save()
            account_form.save()
            return redirect('/')
    return render(request, 'profile/profile-details.html', {
        'form': user_form,
        'account_form': account_form
    })

@login_required
def history(request):
    current_user = request.user
    event = EventModel.objects.filter(author=current_user)
    qs = Reserve.objects.filter(user=current_user)
    return render(request, 'profile/profile-deals.html',{
        'events': event,
        'user': current_user,
        'qs': qs
    })



