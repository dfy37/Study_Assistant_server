from django.db import models

# Create your models here.

# wechat app infomation
class AppInfo(models.Model):
    appid = models.CharField(max_length=50, null=True)
    secret = models.CharField(max_length=50, null=True)
    wechat_url = models.CharField(max_length=100, null=True)


# user's information
class UserInfo(models.Model):
    openid = models.CharField(max_length=50, null=True)
    session_key = models.CharField(max_length=50, null=True)
    user_id = models.CharField(max_length=50, null=True)
    login_time = models.DateTimeField(auto_now_add=True, null=True)
    nick_name = models.TextField(null=True)
    avatar_url = models.TextField(null=True)
    city = models.TextField(null=True)
    country = models.TextField(null=True)
    gender = models.IntegerField(null=True)
    language = models.TextField(null=True)
    province = models.TextField(null=True)
