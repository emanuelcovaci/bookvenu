from django.shortcuts import render_to_response
from post.models import EventModel
from requests.models import RequestModel
# Create your views here.
def home(request):
    if request.user.is_authenticated():
        template = 'homepages/mainpage2.html'
    else:
        template = 'homepages/index.html'
    event=EventModel.objects.all()
    requests=RequestModel.objects.all()
    query = request.GET.get("q")
    if query:
        event=event.filter(adress__contains=query)
    return render_to_response(template, {
        'user': request.user,
        'events':event,
        'requests':requests,
    })
