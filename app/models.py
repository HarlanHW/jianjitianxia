from django.db import models

# 用户基本信息表
#包含用户注册的基本信息
class user(models.Model):
    user_id = models.CharField(max_length=8,primary_key=True)#用户id，主键长度为8
    user_name = models.CharField(max_length=16)#用户名，限制16个字符
    user_password = models.CharField(max_length=16)
    user_sex = models.CharField(max_length=1,choices=['男',"女","其他"],default="其他")
    user_email = models.EmailField
    user_educate_id = models.CharField(max_length=8)
    user_level_id = models.CharField(max_length=8)
    user_intr_id = models.CharField(max_length=8)
    user_status_id = models.CharField(max_length=8)

class educate(models.Model):
    educate_id=models.CharField(max_length=8)
    educate_degree=models.CharField(max_length=8)

class seek(models.Model):
    seek_id = models.CharField(max_length=8,primary_key=True)
    seek_title = models.CharField(max_length=32)
    seek_date = models.DateTimeField()


class level(models.Model):
    level_id = models.CharField()

