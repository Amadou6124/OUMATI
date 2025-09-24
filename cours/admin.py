from django.contrib import admin
from .models import Course, Chapter, Lesson

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1

class ChapterAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ("title", "course", "order")
    ordering = ("course", "order")

class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [ChapterInline]
    list_display = ("title",)
    search_fields = ("title",)

admin.site.register(Course, CourseAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Lesson)
