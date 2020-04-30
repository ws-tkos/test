from django.contrib import admin
from .models import Course, CourseContent, CourseSignIn


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_name", "course_state", "course_content")


@admin.register(CourseContent)
class CourseAdminTwo(admin.ModelAdmin):
    list_display = ("courseId", "chapter", "content_type", "content")


@admin.register(CourseSignIn)
class CourseAdminThree(admin.ModelAdmin):
    list_display = ("courseId", "student_name", "signIn_time")
