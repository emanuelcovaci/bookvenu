from django.shortcuts import render, redirect, render_to_response,get_object_or_404
from django.contrib.auth.decorators import login_required
from forms import CreateEventForm,CommentForm,Edit_Post
from .models import EventModel,Comment
from django.views.decorators.http import require_POST
from django.http import HttpResponse
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import EventModel,Comment
from django.contrib.auth.models import User

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


def get_post(request, slug):
    event = get_object_or_404(EventModel,slug=slug)
    comm_parent = Comment.objects.filter(is_parent=True).filter(post=event)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            parent_obj = None
            try:
                parent_id = Comment.objects.get(id=int(request.POST.get("parent_id")))
            except:
                parent_id = None
            if parent_id:
                parent_qs =Comment.objects.filter(id=parent_id.id)
                if parent_qs:
                    parent_obj = parent_qs.first()
                    comment.is_parent=False
                else:
                    comment.is_parent=True
            comment.post = event
            comment.user = request.user
            comment.parent = parent_obj
            comment.save()
    return render(request, 'posts/Offer-page.html', {'events':event , 'comm_parent':comm_parent, 'user':request.user})

class EventLike(APIView):
    def get(self, request, slug=None,format=None):
        obj = get_object_or_404(EventModel,slug=slug)
        user = self.request.user
        updated = False
        liked = False
        if user.is_authenticated():
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
            else:
                liked = True
                obj.likes.add(user)
            updated = True
        data = {
            "updated": updated,
            "liked": liked
        }
        return Response(data)

class CommentLike(APIView):
    def get(self, request, id,format=None):
        obj = get_object_or_404(Comment,id=id)
        user = self.request.user
        updated = False
        liked = False
        if user.is_authenticated():
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
            else:
                liked = True
                obj.likes.add(user)
            updated = True
        data = {
            "updated": updated,
            "liked": liked
        }
        return Response(data)

def delete_post(request, slug=None):
    EventModel.objects.filter(slug=slug).delete()
    return redirect('/')

def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    post = comment.post
    comment.delete()
    return redirect('post:post-get', slug=post.slug)


def edit(request,slug):
    post = get_object_or_404(EventModel, slug=slug)
    form = Edit_Post(request.POST or None,instance=post, user=request.user)
    if request.method == 'POST':
        if form.is_valid():
           form.save()
           return redirect('/')
    return render(request, 'posts/Edit_post.html', {
        'form': form,
        'post':post,
    })