from django.shortcuts import render
from django.shortcuts import render_to_response
from post.models import EventModel

# Create your views here.
def home(request):
    if request.user.is_authenticated():
        template = 'homepages/mainpage2.html'
    else:
        template = 'homepages/index.html'
    event=EventModel.objects.all()
    return render_to_response(template, {
        'user': request.user,
        'events':event,
    })
