from django.db import models


# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=20)


class AddressInfo(models.Model):
    auser = models.ForeignKey(UserInfo)
    ashou = models.CharField(max_length=50)
    aadd = models.CharField(max_length=100)
    aphone = models.CharField(max_length=11)
    ayoubian = models.CharField(max_length=6)
