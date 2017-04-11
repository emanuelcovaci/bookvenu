from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from forms import CreateEventForm,CommentForm
from .models import EventModel,Comment
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


def get_post(request, name):
    try:
        event = EventModel.objects.get(name=name)
    except EventModel.DoesNotExist:
        raise Http404("Event does not exist")
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = event
            comment.user = request.user.username
            comment.save()
            return redirect('/post/'+event.name)
    else:
        return render(request, 'posts/post-details.html', {"event":event})


