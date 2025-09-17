from django.urls import path
from .views import home , dash, recherche

urlpatterns = [
    path('', home, name='home'),
    path('dash/', dash, name='dash'),
    path('recherche/', recherche, name='recherche'),
]