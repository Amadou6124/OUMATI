from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def dash(request):
    return render(request, 'core/dashboard.html')

def recherche(request):
    return render(request, 'core/recherche.html')