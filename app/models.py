from django.db import models
from django.contrib.auth.models import User
# 说明：所有主键为length为8

# 用户基本信息表
# 包含用户注册的基本信息
class user(models.Model):
    user_id = models.CharField(max_length=8,primary_key=True) #用户id，主键长度为8
    user_name = models.CharField(max_length=16) #用户名，限制16个字符
    user_password = models.CharField(max_length=16) #密码
    user_sex = models.CharField(max_length=1,choices=[(0,"M"),(1,"W"),(2,"X")],default="X")#性别
    user_email = models.CharField(max_length=20,unique=True) #email,主键，可用于登陆
    user_phone = models.CharField(max_length=11,unique=True) #电话号码，主键，可用于登陆
    user_regist_time=models.DateTimeField(auto_now = True)
    user_level_id = models.CharField(max_length=8) #用户等级信息表的主键

#等级信息表,包含基本等级，信用等级，可添加修改
class level(models.Model):
    level_id = models.CharField(max_length=8,primary_key=True)
    level_now = models.CharField(max_length=5)
    level_credit = models.CharField(max_length=5)
    level_money = models.CharField(max_length=10)

#任务信息
class task(models.Model):
    task_id = models.CharField(max_length=8,primary_key=True)
    task_title = models.CharField(max_length=32)
    task_award = models.CharField(max_length=5)
    task_date = models.DateTimeField(auto_now = True)
    task_owner_id = models.CharField(max_length=8)
    task_applyer_id = models.CharField(max_length=8,null=True)
    task_info = models.TextField(null=True)
    task_status_id = models.CharField(max_length=8)

#任务状态
class task_status(models.Model):
    task_status_id = models.CharField(max_length=8,primary_key=True)
    task_status_is_begin = models.CharField(max_length=1)
    task_status_is_end = models.CharField(max_length=1)
    task_status_is_apply = models.CharField(max_length=1)
    task_status_is_agree = models.CharField(max_length=1)
    task_status_publish_time = models.DateTimeField()
    task_status_begin_time = models.DateTimeField()
    task_status_finish_time = models.DateTimeField()
    task_status_apply_time = models.DateTimeField()
    task_status_agree_time = models.DateTimeField()

#招聘信息
class employ(models.Model):
    employ_id = models.CharField(max_length=8,primary_key=True)
    employ_title = models.CharField(max_length=32)
    employ_date = models.DateTimeField()
    employ_owner = models.CharField(max_length=8)
    employ_info = models.TextField()



