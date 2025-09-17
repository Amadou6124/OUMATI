from django.shortcuts import render, redirect
from .forms import ContactMessage

# Create your views here.
def contact(request):
    if request.method == "POST":
        form = ContactMessage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactMessage()
    return render(request, 'revision/contact.html', {'form': form})