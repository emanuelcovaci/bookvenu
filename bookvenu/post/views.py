from django.shortcuts import render, redirect

from forms import EventForm
# Create your views here.
def create_post(request):
    form = EventForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, "posts/post.html", {
        'form': form
    })

def post(request):
    return render(request, 'posts/Offer-page.html')