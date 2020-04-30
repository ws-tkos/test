from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from course import views
from django.contrib.auth.models import User, Group
from .forms import RegisterForm


# 跳转到登陆页
def loginPage(request):
    context = {}
    return render(request, 'login_page.html', context)


# 基础页面测试
def base(request):
    context = {}
    return render(request, 'base.html', context)


# 登录功能
def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
        auth.login(request, user)
        # Redirect to a success page.
        return redirect(views.index)
    else:
        # Return an 'invalid login' error message.
        context = {'message': '用户名或密码不正确。'}
        return render(request, 'login_page.html', context)


# 登出功能
def logout_view(request):
    auth.logout(request)
    return render(request, 'login_page.html')


# 跳转到注册页面
def register_view(request):
    register_form = RegisterForm()
    context = {'register_form': register_form}
    return render(request, 'register.html', context)


# 注册功能
def register(request):
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():     # 验证通过
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            first_name = reg_form.cleaned_data['nickname']
            # 创建用户
            user = User.objects.create_user(username, email=email, password=password, first_name=first_name)
            user.save()
            # 添加用户到student组
            student_group = Group.objects.get(name="student")
            this_user = User.objects.get(username=username)
            student_group.user_set.add(this_user)
            # 返回登录页面
            context = {'message': '注册成功，请登录。'}
            return render(request, 'login_page.html', context)
    else:
        reg_form = RegisterForm()
        context = {'reg_form': reg_form}
        return render(request, 'register.html', context)


def jupyter(request):
    context = {}
    return render(request, 'course/jupyter.html', context)
