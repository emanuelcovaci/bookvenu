from .models import RequestModel
from django.contrib.auth.decorators import login_required
from .forms import CreateRequestForm
from django.shortcuts import render, redirect
# Create your views here.
@login_required
def create_request(request):
    current_user = request.user
    form = CreateRequestForm(request.POST or None,user=current_user)
    if request.method == 'POST':
        if form.is_valid():
            request = form.instance
            request.autor = current_user
            form.save()
            return redirect('/')
    return render(request, "posts/request.html", {
        'user': request.user,
        'form': form,
    })

@login_required
def delete_requests(request, slug=None):
    RequestModel.objects.filter(slug=slug).delete()
    return redirect('/')