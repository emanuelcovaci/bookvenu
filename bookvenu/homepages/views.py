from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def home(request):
    if request.user.is_authenticated():
        template = 'homepages/mainpage2.html'
    else:
        template = 'homepages/index.html'
    return render_to_response(template, {
        'user': request.user,
    })
