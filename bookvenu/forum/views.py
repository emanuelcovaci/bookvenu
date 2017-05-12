from .models import Thread,ThreadComment
from .forms import ThreadForm,ThreadCommentForm
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.shortcuts import render, redirect, render_to_response,get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.http import HttpResponse
# Create your views here.
def forum_home(request):
    threads=Thread.objects.all()
    form = ThreadForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            post=form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/forum')
    if request.method == 'GET':
        query = request.GET.get("q")
        if query:
            threads=Thread.objects.filter(name__contains=query)
    return render(request, 'forum/home.html', {
        'user': request.user,
        'threads':threads,
        'form':form
    })
def forum_thread(request,slug):
    thread = get_object_or_404(Thread,slug=slug)
    comm_parent = ThreadComment.objects.filter(is_parent=True).filter(post=thread)
    if request.method == "POST":
        form = ThreadCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            parent_obj = None
            try:
                parent_id = ThreadComment.objects.get(id=int(request.POST.get("parent_id")))
            except:
                parent_id = None
            if parent_id:
                parent_qs =ThreadComment.objects.filter(id=parent_id.id)
                if parent_qs:
                    parent_obj = parent_qs.first()
                    comment.is_parent=False
                else:
                    comment.is_parent=True
            comment.post = thread
            comment.user = request.user
            comment.parent = parent_obj
            comment.save()
    return render(request, 'forum/thread-page.html', {'thread':thread , 'comm_parent':comm_parent, 'user':request.user})
class ThreadLike(APIView):
    def get(self, request, slug=None,format=None):
        obj = get_object_or_404(Thread,slug=slug)
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

class ThreadcomLike(APIView):
    def get(self, request, id=None,format=None):
        obj = get_object_or_404(ThreadComment,id=id)
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

def thread_delete(request, slug=None):
    Thread.objects.filter(slug=slug).delete()
    return redirect('/')

def threadcom_delete(request, id):
    comment=ThreadComment.objects.get(id=id)
    post = comment.post
    comment.delete()
    return redirect("forum:forum-thread", slug=post.slug)