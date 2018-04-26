from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import datetime
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import forms
from django.utils.timezone import now,timedelta
from app import models
from django.db.models import Q
import time
# 主页
def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, "index.html")

# 登陆功能
def sign_in(request):
    ctx = {}
    if request.POST:
        name = request.POST['name']
        password = request.POST['password']
        print(name)
        print(password)
        return render(request,"index.html")
    else:
        return render(request,"sign_in.html")

#注册功能
def sign_up(request):
    ctx = {}
    if request.method=='POST':#接收到页面请求
        username = request.POST['name']
        email=request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        sex = request.POST['sex']
        phone = request.POST['phone']
        if password1==password2:#若信息无误，则创建成功，并跳转到登录界面
            print(username)
            print(email)
            print(password1)
            print(password2)
            print(sex)
            print(phone)
            new_user =models.user.objects.create(user_name=username,user_password=password1,
                                                 user_phone=phone,user_sex=sex,user_email=email)

            return HttpResponseRedirect('sign_in')
        else:
            return HttpResponseRedirect('home')
    else:
        return render(request,'sign_up.html')

#显示主页面