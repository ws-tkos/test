from django.shortcuts import render, redirect
from .models import Comment
from course.models import CourseContent
from django.urls import reverse
from .forms import CommentForm


# 提交评论
def update_comment(request):
    # user = request.user
    # text = request.POST.get('text', '').strip()
    # course_id = int(request.POST.get('course_id', ''))
    # chapter_num = int(request.POST.get('chapter_num', ''))
    # comment = Comment()
    # comment.user = user
    # comment.text = text
    # comment.course_id = course_id
    # comment.chapter_num = chapter_num
    # comment.save()
    # referer = request.META.get('HTTP_REFERER', reverse('course_chapter', kwargs={'course_id': course_id, 'chapter_num': chapter_num}))
    # return redirect(referer)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = Comment()
        # 获取form值
        user = request.user
        course_id = comment_form.cleaned_data['course_id']
        chapter_num = comment_form.cleaned_data['chapter_num']
        text = comment_form.cleaned_data['text']
        # 赋值给model
        comment.user_id = user.id
        comment.text = text
        comment.course_id = course_id
        comment.chapter_num = chapter_num
        comment.save()
        referer = request.META.get('HTTP_REFERER', reverse('course_chapter', kwargs={'course_id': course_id, 'chapter_num': chapter_num}))
        return redirect(referer)


def update_chapter(request):
    chapter_form = CommentForm(request.POST)
    if chapter_form.is_valid():
        chapter = CourseContent()
        # 获取form值
        course_id = chapter_form.cleaned_data['course_id']
        chapter_num = chapter_form.cleaned_data['chapter_num']
        text = chapter_form.cleaned_data['text']
        # 赋值给model
        chapter.courseId = course_id
        chapter.chapter = chapter_num
        chapter.content = text
        chapter.save()
        referer = request.META.get('HTTP_REFERER', reverse('course_chapter',
                                                           kwargs={'course_id': course_id, 'chapter_num': 1}))
        return redirect(referer)

