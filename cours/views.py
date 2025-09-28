from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Course, Lesson, LessonProgress


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    # Charger la première vidéo par défaut
    first_video = None
    first_chapter = course.chapters.first()
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




def lesson_detail(request, course_id, lesson_id):
    course = get_object_or_404(Course, id=course_id)
    lesson = get_object_or_404(Lesson, id=lesson_id, chapter__course=course)

    # ✅ Marquer la leçon comme terminée si user connecté
    if request.user.is_authenticated:
        progress, created = LessonProgress.objects.get_or_create(user=request.user, lesson=lesson)
        if not progress.completed:
            progress.completed = True
            progress.save()

    # Toutes les leçons du cours dans l'ordre
    all_lessons = []
    for chapter in course.chapters.order_by('order').prefetch_related('lessons'):
        all_lessons.extend(list(chapter.lessons.all()))

    idx = all_lessons.index(lesson)
    prev_lesson = all_lessons[idx-1] if idx > 0 else None
    next_lesson = all_lessons[idx+1] if idx < len(all_lessons)-1 else None

    # ✅ Récupérer toutes les leçons terminées par l'utilisateur
    completed_lessons = []
    if request.user.is_authenticated:
        completed_lessons = LessonProgress.objects.filter(
            user=request.user, completed=True
        ).values_list("lesson_id", flat=True)

    return render(
        request,
        "cours/course_detail.html",
        {
            "course": course,
            "first_video": lesson,
            "prev_lesson": prev_lesson,
            "next_lesson": next_lesson,
            "completed_lessons": completed_lessons,  # ✅ envoyé au template
        }
    )



from django.http import JsonResponse, request
from django.views.decorators.csrf import csrf_exempt
from .models import LessonProgress, Lesson

@csrf_exempt
def mark_lesson_completed(request, lesson_id):
    if request.user.is_authenticated and request.method == "POST":
        lesson = get_object_or_404(Lesson, id=lesson_id)
        progress, created = LessonProgress.objects.get_or_create(user=request.user, lesson=lesson)
        progress.completed = True
        progress.save()
        return JsonResponse({"status": "ok"})

    return JsonResponse({"status": "unauthorized"}, status=401)
    
