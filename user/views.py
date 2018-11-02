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


class SignUpView(CreateView):
    """
    注册视图
    """
    model = UserProfile
    form_class = SignupForm
    template_name = 'user/signup.html'

    def post(self, request, *args, **kwargs):
        has_error = True
        if request.POST.get('checkcode', None):
            # 判断验证码
            # print(request.session['CheckCode'])
            # print(request.POST.get('checkcode'))
            if request.session['CheckCode'].upper() == request.POST.get('checkcode').upper():
                # Form验证
                obj = SignupForm(request.POST)
                print(obj)
                # if obj.is_valid():
                #     has_error = False
                #     username = obj.cleaned_data['username']
                #     password = obj.cleaned_data['password']
                #     email = obj.cleaned_data['email']
                #     mobile = obj.cleaned_data['mobile']
                #     # 保存用户
                #     user_obj = UserProfile()
                #     user_obj.username = username
                #     user_obj.email = email
                #     user_obj.mobile = mobile
                #     user_obj.set_password(password)
                #     print(user_obj)
                #     user_obj.save()
                #     # 注册成功，创建用户details 表
                #     # UserDetails.objects.create(user_id=user_obj.id)
                #     login(request, user_obj)
                #     return redirect(reverse('home'))
                has_error = False
                username = obj.cleaned_data['username']
                password = obj.cleaned_data['password']
                email = obj.cleaned_data['email']
                mobile = obj.cleaned_data['mobile']
                # 保存用户
                user_obj = UserProfile()
                user_obj.username = username
                user_obj.email = email
                user_obj.mobile = mobile
                user_obj.set_password(password)
                print(user_obj)
                user_obj.save()
                # 注册成功，创建用户details 表
                # UserDetails.objects.create(user_id=user_obj.id)
                login(request, user_obj)
                return redirect(reverse('home'))
            else:
                code_error = "验证码错误"
                return redirect('user:signup')
        else:
            code_error = "请输入验证码"
        # return render(request, 'user/signup.html', locals())
        return redirect('user:signup')

    # def form_valid(self, form):
    #
    #     # 比较验证码
    #     # 存入数据库
    #     user = form.save()
    #     print('验证成功')
    #     login(self.request, user)
    #     return redirect('home')




class LoginView(View):
    pass
