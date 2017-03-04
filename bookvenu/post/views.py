from django.shortcuts import render

# Create your views here.
def create_post(request):
    return render(request, 'posts/post.html')
def post(request):
    return render(request, 'posts/Offer-page.html')