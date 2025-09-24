from django.contrib import admin
from .models import SpecialOffer, Category, Course

@admin.register(SpecialOffer)
class SpecialOfferAdmin(admin.ModelAdmin):
    list_display = ("title", "badge", "offer_text", "created_at")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "icon", "color")

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "views", "created_at", 'image')
    list_filter = ("category",)
