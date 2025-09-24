from django.shortcuts import render, get_object_or_404
from .models import Course

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    # Récupérer la première leçon vidéo
    first_video = None
    first_chapter = course.chapters.first()  # ok en Python
    if first_chapter:
        first_video = first_chapter.lessons.first()
    
    return render(
        request,
        "cours/course_detail.html",
        {
            "course": course,
            "first_video": first_video
        }
    )
