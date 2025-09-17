from django.urls import path
from .views import video, mon


urlpatterns = [
    path('video/', video, name="video"),
    path('mon/', mon, name="mon"),
]