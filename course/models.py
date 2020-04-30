from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Course(models.Model):
    course_name = models.CharField(max_length=100)      # 课程名称
    course_content = models.TextField()     # 课程简介
    course_state = models.BooleanField(default=False)       # 课程状态

    def __str__(self):
        return "<Course: %s>" % self.course_name


class CourseContent(models.Model):
    courseId = models.IntegerField()
    chapter = models.IntegerField()
    content_type = models.CharField(max_length=100, default="text")
    content = RichTextUploadingField()


class CourseSignIn(models.Model):
    courseId = models.IntegerField()
    student_id = models.IntegerField()
    student_name = models.TextField(max_length=100)
    signIn_time = models.DateField(auto_now=True)
