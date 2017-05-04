from django.shortcuts import render,redirect
from .forms import ContactForm

# Create your views here.
def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            contact = form.instance
            contact.user = request.user
            form.save()
            return redirect('/')
    return render(request, 'contact/contact.html', {'form':form})