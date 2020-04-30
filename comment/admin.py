from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'chapter_num', 'comment_time', 'user', 'text')
