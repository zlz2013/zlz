from django.db import models

# Create your models here.
#file:bookstore/models.py

class Book(models.Model):
    title=models.CharField('书名',max_length=50)
    pub=models.CharField('出版社',max_length=50)
    price=models.DecimalField('定价',max_digits=7,decimal_places=2,default=0.0)
    pub_date=models.DateField('出版时间',
                              # auto_now_add=True,
                              # default='2019-1-1',
                              auto_now=True,
                              )

class Author(models.Model):
    name=models.CharField('作者名',max_length=30)
    age=models.IntegerField('年龄')
