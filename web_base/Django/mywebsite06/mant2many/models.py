from django.db import models

# Create your models here.


class Author3(models.Model):
    name=models.CharField('姓名',max_length=50)
    def __str__(self):
        return '姓名:'+self.name

class Book3(models.Model):
    title=models.CharField('书名',max_length=50)
    author=models.ManyToManyField(Author3,null=True)
    def __str__(self):
        return '书名:'+self.title