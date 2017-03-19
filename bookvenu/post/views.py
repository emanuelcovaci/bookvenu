from django.shortcuts import render, redirect

from forms import EventForm
# Create your views here.
def create_post(request):
    form = EventForm(request.POST)
    print "create post"
    if request.method == 'POST':
        if form.is_valid() == True:
            form.save()
        return redirect('/')
    return render(request, "posts/post.html", {
        'form': form,
    })

def post(request):
    return render(request, 'posts/Offer-page.html')