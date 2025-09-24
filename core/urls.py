from django.urls import path
from .views import home , dash, search_view, search_result, course_detail, category_detail

urlpatterns = [
    path('', home, name='home'),
    path('dash/', dash, name='dash'),
    path('recherche/', search_view, name='recherche'),
    path('search_result/', search_result, name='search_result'),
    path("categories/<int:pk>/", category_detail, name="category_detail"),
    path("courses/<int:pk>/", course_detail, name="course_detail"),
]