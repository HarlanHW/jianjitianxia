from django.shortcuts import render


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

