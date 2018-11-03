from io import BytesIO
from datetime import datetime

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login
from django.urls import reverse
from django.core.cache import cache
from django.http import Http404
from django.db.models import Q
from django.views.generic import (
    CreateView, View
)
from django.views.generic.edit import FormView, ProcessFormView
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm

from .models import UserProfile
from .forms import SignupForm, LoginForm
from utils.captcha import create_validate_code


def check_code(request):
    """
    验证码
    :param request:
    :return:
    """
    stream = BytesIO()
    img, code = create_validate_code()
    img.save(stream, 'PNG')
    request.session['CheckCode'] = code
    return HttpResponse(stream.getvalue())


class UserSignUpView(CreateView):
    """
    注册视图
    """
    model = UserProfile
    form_class = SignupForm
    template_name = 'user/signup.html'

    def form_valid(self, form):
        # 比较验证码
        # 存入数据库
        # print(self.request.session['CheckCode'])
        # print(self.request.POST.get('check_code'))
        if self.request.session['CheckCode'].upper() == self.request.POST.get('check_code').upper():
            # print('验证码相同')
            user = form.save()
            # print('验证成功')
            login(self.request, user)
            return redirect('home')
        else:
            return redirect('user:signup')


class UserLoginView(CreateView):
    """
    注册视图
    """
    model = UserProfile
    form_class = LoginForm
    template_name = 'user/login.html'

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     return self.form_valid(form)

    def form_valid(self, form):
        # 比较验证码
        # 存入数据库
        print(self.request.session['CheckCode'])
        print(self.request.POST.get('check_code'))
        if self.request.session['CheckCode'].upper() == self.request.POST.get('check_code').upper():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = UserProfile.objects.filter(Q(username=username) | Q(password=password))
            login(self.request, user)
            return redirect('home')
        else:
            return redirect('user:login')

    def form_invalid(self, form):
        print('无效输入')
        print(form)
        print(self.request.session['CheckCode'])
        print(self.request.POST.get('check_code'))
        if self.request.session['CheckCode'].upper() == self.request.POST.get('check_code').upper():
            username = self.request.POST.get('username')
            password = self.request.POST.get('password')
            user = UserProfile.objects.filter(Q(username=username) | Q(password=password)).first()
            login(self.request, user)
            return redirect('home')
        else:
            return redirect('user:login')






