from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from forms import CreateEventForm
from .models import EventModel
# Create your views here.

@login_required
def create_post(request):
    current_user = request.user
    form = CreateEventForm(request.POST or None, request.FILES or None,user=current_user)
    if request.method == 'POST':
        if form.is_valid():
            post = form.instance
            post.author = current_user
            form.save()
            return redirect('/')
    return render(request, "posts/post.html", {
        'form': form,

    })


@login_required
def post(request):
    event=EventModel.objects.all()
    return render(request, "posts/Offer-page.html", {
        'events': event,
    })


