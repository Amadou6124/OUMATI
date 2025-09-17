from django.http import request
from django.shortcuts import render

# Create your views here.
def video(request):
    return render(request, 'cours/videos.html')

def mon(requwst):
    return render(request, 'cours/mon.html')