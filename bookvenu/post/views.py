from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from forms import EventForm
from .models import EventModel
# Create your views here.

@login_required
def create_post(request):
    form = EventForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
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


