"""weblearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.loginPage, name='home'),
    path('register_view/', views.register_view, name='register_view'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('base/', views.base),
    path('admin/', admin.site.urls),
    path('course/', include("course.urls")),
    path('comment/', include("comment.urls")),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('jupyter/', views.jupyter, name='jupyter'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL, doucument_root=settings.MEDIA_ROOT)
