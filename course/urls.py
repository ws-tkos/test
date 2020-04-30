from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="webindex"),
    # path('course/<int:course_id>/', views.course_detail, name="course_detail"),
    path('course_list/', views.course_list, name="course_list"),
    path('course/<int:course_id>/chapter/<int:chapter_num>/', views.course_chapter, name="course_chapter"),
    path('chapter_add/<int:course_id>/', views.course_chapter_add, name="course_chapter_add"),
    path('course_list/<int:course_id>/', views.signIn, name='signIn'),
    path('course_manage/', views.course_manage, name='course_manage'),
    path('courseAdd/<int:course_id>', views.courseAdd, name='courseAdd'),
    path('courseRemove/<int:course_id>', views.courseRemove, name='courseRemove'),
    path('courseStop/<int:course_id>', views.courseStop, name='courseStop'),
    path('courseOpen/<int:course_id>', views.courseOpen, name='courseOpen'),
    path('student_manage/', views.student_manage, name='student_manage'),
]
