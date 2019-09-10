from django.db import models

# Create your models here.


# file : bookstore/models.py
from django.db import models


class Book(models.Model):
    title = models.CharField("书名", max_length=50, default="untitled")
    pub = models.CharField("出版社", max_length=100, default='')
    price = models.DecimalField('定价', max_digits=7, decimal_places=2, default=0.0)
    market_price = models.DecimalField('零售价', max_digits=7, decimal_places=2, default=9999)


    def __str__(self):
        return "书名:" + self.title

    class Meta:
        pass

class Author(models.Model):
    name=models.CharField('作者名',max_length=30,unique=True,db_index=True)
    age=models.IntegerField('年龄',default=1)
    email=models.EmailField('邮箱',null=True)
    class Meta:
        # db_table = 'author'
        pass
    def __str__(self):
        return "作者:" + self.name

class Wife(models.Model):
    name = models.CharField('作者妻子', max_length=30)
    author=models.OneToOneField(Author,null=True)
    age = models.IntegerField('年龄', default=1)
    email = models.EmailField('邮箱', null=True)

    def __str__(self):
        return "作者妻子:" + self.name