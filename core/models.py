# models.py

from django.db import models

class SpecialOffer(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    badge = models.CharField(max_length=100, blank=True, null=True)
    offer_text = models.CharField(max_length=100, blank=True, null=True)
    background = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_background(self):
        """Retourne le background ou un gradient par défaut"""
        if self.background:
            return self.background
        # Gradients par défaut basés sur l'index (optionnel)
        gradients = [
            "linear-gradient(135deg, #6f42c1 0%, #4a2a8d 100%)",
            "linear-gradient(135deg, #fd7e14 0%, #c25c00 100%)",
            "linear-gradient(135deg, #20c997 0%, #13855c 100%)"
        ]
        return gradients[self.id % len(gradients)] if self.id else gradients[0]


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)  # ex: "fas fa-hands-praying"
    color = models.CharField(max_length=50, blank=True, null=True)  # ex: "#6f42c1"

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="courses")
    thumbnail_url = models.URLField(blank=True, null=True)  # lien YouTube ou autre
    image = models.ImageField(upload_to="courses/", blank=True, null=True)  # upload local
    duration = models.CharField(max_length=20, blank=True, null=True)  # ex: "12:45"
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

# models.py
class PopularSearch(models.Model):
    term = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.term