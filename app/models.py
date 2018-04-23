from django.db import models

# 说明：所有主键为length为8

# 用户基本信息表
# 包含用户注册的基本信息
class user(models.Model):
    user_id = models.CharField(max_length=8,primary_key=True) #用户id，主键长度为8
    user_name = models.CharField(max_length=16) #用户名，限制16个字符
    user_password = models.CharField(max_length=16) #密码
    user_sex = models.CharField(max_length=1,choices=[(0,"M"),(1,"W"),(2,"X")],default="X")#性别
    user_email = models.CharField(max_length=20,primary_key=True) #email,主键，可用于登陆
    user_phone = models.CharField(max_length=11,primary_key=True) #电话号码，主键，可用于登陆
    user_educate_id = models.CharField(max_length=8) #教育信息表
    user_level_id = models.CharField(max_length=8) #用户等级信息表的主键
    user_intr_id = models.CharField(max_length=8) #用户介绍信息的主键
    user_status_id = models.CharField(max_length=8) #用户状态信息的主键
    user_company_id = models.CharField(max_length=8) #用户公司信息

#等级信息表,包含基本等级，信用等级，可添加修改
class level(models.Model):
    level_id = models.CharField(max_length=8,primary_key=True)
    level_now = models.CharField(max_length=5)
    level_credit = models.CharField(max_length=5)

class educate(models.Model):
    educate_id=models.CharField(max_length=8)
    educate_degree=models.CharField(max_length=8)

class seek(models.Model):
    seek_id = models.CharField(max_length=8,primary_key=True)
    seek_title = models.CharField(max_length=32)
    seek_date = models.DateTimeField()


class level(models.Model):
    level_id = models.CharField(max_length=8)
