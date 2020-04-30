from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


class Comment(models.Model):
    # 评论对象
    course_id = models.IntegerField()
    chapter_num = models.IntegerField()
    # 评论时间
    comment_time = models.DateTimeField(auto_now_add=True)
    # 评论用户
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # 评论内容
    text = models.TextField()

    class Meta:
        ordering = ['-comment_time']
