from django.shortcuts import render
from django.http import HttpResponse

# 主页
def home(request):
    return render(request, "index.html")

# 注册功能
def registe(request):
    name="1"
    passwd="1"
    return 1

# 登陆功能
def login(request):
    ctx = {}
    if request.POST:
        name = request.POST['email']
        password = request.POST['password']
        print(name)
        print(password)
        return render(request,"index.html")
    else:
        return render(request,"login.html")

#注册功能
def sign_up(request):
    ctx = {}
    if request.POST:  # 接收到页面请求
        username = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(username)
        print(email)
        print(password1)
        print(password2)
        #if password1 == password2:  # 若信息无误，则创建成功，并跳转到登录界面
            #user = User.objects.create_user(username=_username, email=_email, password=_password1)
            #    Referee.objects.create(user=user, Rname=_Rname, Rsex=_Rsex, Rgrade=_Rgrade, Rdetp=_Rdept, Rlevel="new")
            #    RefereeTime.objects.create(user=user)
        return render(request,"index.html")
        #else:
        #    return HttpResponse("fail")
    else:
        return render(request,"sign_up.html")

#显示主页面