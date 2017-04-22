from django.shortcuts import render, redirect, render_to_response,get_object_or_404
from django.contrib.auth.decorators import login_required
from forms import CreateEventForm,CommentForm
from .models import EventModel,Comment
from django.views.decorators.http import require_POST
from django.http import HttpResponse
try:
    from django.utils import simplejson as json
except ImportError:
    import json

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
def post(request,slug):

    event = get_object_or_404(EventModel, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = event
            comment.user = request.user.username
            comment.save()
    return render(request, "posts/Offer-page.html", {
        'events': event,

    })

@login_required
@require_POST
def like(request):
    if request.method == 'POST':
        user = request.user
        slug = request.POST.get('slug', None)
        company = get_object_or_404(EventModel, slug=slug)

        if company.likes.filter(id=user.id).exists():
            # user has already liked this company
            # remove like/user
            company.likes.remove(user)
            message = 'You disliked this'
        else:
            # add a new like for a company
            company.likes.add(user)
            message = 'You liked this'

    ctx = {'likes_count': company.total_likes, 'message': message}
    # use mimetype instead of content_type if django < 5
    return HttpResponse(json.dumps(ctx), content_type='application/json')



