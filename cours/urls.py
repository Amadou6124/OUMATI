from django.urls import path
from . import views

urlpatterns = [
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('<int:course_id>/lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path("lessons/<int:lesson_id>/complete/", views.mark_lesson_completed, name="mark_lesson_completed"),
]
