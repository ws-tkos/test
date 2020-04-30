from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, CourseContent, CourseSignIn
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import Group, Permission, User
from comment.models import Comment
from comment.forms import CommentForm


# 跳转到首页
def index(request):
    context = {'courses': Course.objects.all()}
    return render(request, 'course/index.html', context)


# 跳转到课程列表
def course_list(request):
    context = {'courses': Course.objects.all()}
    return render(request, 'course/course_list.html', context)


# 跳转到课程详情
# def course_detail(request, course_id):
#     context = {"course": get_object_or_404(Course, id=course_id),
#                "chapters": CourseContent.objects.filter(courseId=int(course_id))}
#     return render(request, 'course/course_detail.html', context)


# 跳转到课程章节
def course_chapter(request, course_id, chapter_num):
    sign_info = CourseSignIn.objects.filter(courseId=int(course_id), signIn_time=timezone.now(), student_id=request.user.id)
    sign_bool = 0
    if sign_info.exists():
        sign_bool = 1
    context = {"course": get_object_or_404(Course, id=course_id),
               "chapters": CourseContent.objects.filter(courseId=int(course_id)),
               "thisChapter": get_object_or_404(CourseContent, courseId=int(course_id), chapter=chapter_num),
               "signInBool": sign_bool,
               "comments": Comment.objects.filter(course_id=int(course_id), chapter_num=int(chapter_num)),
               "comment_form": CommentForm(initial={
                   "course_id": course_id,
                   "chapter_num": chapter_num})
               }
    return render(request, 'course/course_detail.html', context)


# 跳转到课程章节添加页面
def course_chapter_add(request, course_id):
    next_chapter_num = CourseContent.objects.filter(courseId=int(course_id)).count() + 1
    context = {"course": get_object_or_404(Course, id=course_id),
               "chapters": CourseContent.objects.filter(courseId=int(course_id)),
               "comment_form": CommentForm(initial={
                   "course_id": course_id,
                   "chapter_num": next_chapter_num})
               }
    return render(request, 'course/course_chapter_add.html', context)


# 用户签到
def signIn(request, course_id):
    sig_in = CourseSignIn.objects.create(courseId=course_id, student_id=request.user.id, student_name=request.user.first_name)
    referer = request.META.get('HTTP_REFERER', reverse('course_chapter', kwargs={'course_id': 1, 'chapter_num': 1}))
    return redirect(referer)


# 跳转到课程管理
def course_manage(request):
    context = {'courses': Course.objects.all()}
    return render(request, 'course/course_manage.html', context)


# 课程添加
def courseAdd(request, course_id):
    my_group = Group.objects.get(name=course_id)
    my_group.user_set.add(request.user)
    referer = request.META.get('HTTP_REFERER', reverse('course_manage'))
    return redirect(referer)


# 课程退选
def courseRemove(request, course_id):
    my_group = Group.objects.get(name=course_id)
    my_group.user_set.remove(request.user)
    referer = request.META.get('HTTP_REFERER', reverse('course_manage'))
    return redirect(referer)


# 暂停课程
def courseStop(request, course_id):
    my_course = Course.objects.get(id=course_id)
    my_course.course_state = 0
    my_course.save()
    referer = request.META.get('HTTP_REFERER', reverse('course_manage'))
    return redirect(referer)


# 开始课程
def courseOpen(request, course_id):
    my_course = Course.objects.get(id=course_id)
    my_course.course_state = 1
    my_course.save()
    referer = request.META.get('HTTP_REFERER', reverse('course_manage'))
    return redirect(referer)


# 学生管理页面
def student_manage(request):
    context = {}
    course_id = 1
    context["courses"] = Course.objects.all()
    context["signIn"] = CourseSignIn.objects.filter(signIn_time=timezone.now())
    while course_id > 0:
        # 遍历课程
        group = Group.objects.filter(name=course_id)
        if group.exists():
            # 课程存在
            context["course_sum"] = Course.objects.all().count()
            context["users"+str(course_id)] = User.objects.filter(groups__in=str(course_id))
            course_id += 1
        else:
            break
    return render(request, 'course/student_manage.html', context)
