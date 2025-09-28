from django.db import models
from django.urls import reverse
from django.conf import settings

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    prerequisites = models.TextField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)  # image (poster du lecteur vidéo)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    course = models.ForeignKey(Course, related_name="chapters", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.course.title} - {self.title}"


class Lesson(models.Model):
    LESSON_TYPE_CHOICES = [
        ("video", "Vidéo"),
        ("text", "Texte"),
        ("quiz", "Quiz"),
    ]

    chapter = models.ForeignKey(Chapter, related_name="lessons", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    lesson_type = models.CharField(max_length=20, choices=LESSON_TYPE_CHOICES, default="video")
    youtube_url = models.URLField(blank=True, null=True)
    duration = models.CharField(max_length=20, blank=True, null=True)  # ex: "4m 20s"
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.chapter.title} - {self.title}"

    # ✅ Nouvelle méthode
    def youtube_id(self):
        """Retourne uniquement l'ID de la vidéo YouTube"""
        if not self.youtube_url:
            return None

        import re
        # 1. Si c’est déjà un ID pur
        if len(self.youtube_url) == 11 and re.match(r'^[a-zA-Z0-9_-]{11}$', self.youtube_url):
            return self.youtube_url

        # 2. Sinon, essayer de trouver l’ID dans l’URL
        match = re.search(r"(?:v=|\/embed\/|\.be\/)([a-zA-Z0-9_-]{11})", self.youtube_url)
        return match.group(1) if match else None
    
    def get_absolute_url(self):
        return reverse("lesson_detail", args=[self.chapter.course.id, self.id])

    @property
    def youtube_id(self):
        if not self.youtube_url:
            return None
        import urllib.parse
        url_data = urllib.parse.urlparse(self.youtube_url)
        query = urllib.parse.parse_qs(url_data.query)
        return query.get("v", [None])[0]
    
class LessonProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lesson = models.ForeignKey("Lesson", on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "lesson")  # un seul enregistrement par utilisateur/leçon

    def __str__(self):
        return f"{self.user} - {self.lesson} ({'✓' if self.completed else '✗'})"