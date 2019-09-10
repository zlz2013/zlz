from django.db import models

# Create your models here.


#不在使用此模型类来记录数据
class User(models.Model):
    username=models.CharField('用户名',max_length=30)
    password=models.CharField('密码',max_length=30)

    def __str__(self):
        return '用户:'+self.username