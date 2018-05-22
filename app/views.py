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


def index(request):
    return render(request, "index.html")


@login_required(login_url='sign_in.html')#判断是否登录，若没有登录则跳转到登录界面
def publish(request):
    user_User = User.objects.get(username=request.user.username)
    user = models.user.objects.get(user_user=user_User)
    if request.POST:
        if 'title' in request.POST:
            task_id = models.task.objects.latest('task_id').task_id;
            task_id=int(task_id)
            task_id+=1;
            task_title = request.POST['title']
            task_award = request.POST['award']
            task_date = now()
            task_owner_id = user.user_id
            task_status_id = str(task_id)
            task_info = request.POST['info']
            task=models.task.objects.create(task_id=str(task_id),task_title=task_title,task_award=task_award,
                                            task_date=task_date,task_owner_id=task_owner_id,
                                            task_status_id=task_status_id,task_info=task_info)
            task_status=models.task_status.objects.create(task_status_id=task_status_id,task_status_is_begin='0',
                                                          task_status_is_apply='0',task_status_is_agree='0',
                                                          task_status_is_end='0',
                                                          task_status_publish_time=now())
                                                          #task_status_begin_time="",
                                                          #task_status_apply_time="",
                                                          #task_status_agree_time="",
                                                          #task_status_finish_time="")
            return HttpResponse("任务发布成功")
        else:
            return render(request, "publish.html", {"user": user})

    else:
        return render(request, "publish.html", {"user": user})

# 信息页面
@login_required(login_url='sign_in.html')#判断是否登录，若没有登录则跳转到登录界面
def home(request):
    user_User = User.objects.get(username=request.user.username)
    user = models.user.objects.get(user_user=user_User)
    if request.POST:
        return HttpResponseRedirect('publish')
    else:
        return render(request,"home.html",{"user":user})

# 登陆功能
def sign_in(request):
    ctx = {}
    if request.POST:
        name = request.POST['name']
        password = request.POST['password']
        user_User = authenticate(username=name, password=password)
        if user_User is not None:  # 在数据库中查询，若信息正确则登录跳转到相应界面，否则停留在登录界面
            login(request, user_User)
            user_User = User.objects.get(username=name)
            user = models.user.objects.get(user_user=user_User)
            return HttpResponseRedirect('home')
        else:
            return HttpResponse("用户名或密码错误")
    else:
        return render(request, 'sign_in.html')

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
            id = User.objects.latest('id').id+1
            user_User = User.objects.create_user(username=username, email=email, password=password1)
            models.user.objects.create(user_id=id,user_user=user_User,user_name=username,user_phone=phone,
                                       user_sex=sex,user_email=email)
            return HttpResponseRedirect('sign_in')
        else:
            return render(request,'sign_up.html')
    else:
        return render(request, 'sign_up.html')
