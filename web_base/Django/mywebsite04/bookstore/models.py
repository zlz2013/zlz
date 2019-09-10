from django.db import models

# Create your models here.
#file:bookstore/models.py

class Book(models.Model):
    title=models.CharField('书名',max_length=50)
    pub=models.CharField('出版社',max_length=50)
    price=models.DecimalField('定价',max_digits=7,
                              decimal_places=2,default=0.0)
    market_price=models.DecimalField('零售价',max_digits=7,
                                     decimal_places=2,default=999)
    pub_date=models.DateField('出版时间',
                              auto_now_add=True,
                              # default='2019-1-1',
                              # auto_now=True,
                              )
    def __str__(self):
        return '书名：'+self.title+'出版社:'+self.pub

class Author(models.Model):
    name=models.CharField('作者名',max_length=30,unique=True,db_index=True)
    age=models.IntegerField('年龄',default=1)
    email=models.EmailField('邮箱',null=True)
