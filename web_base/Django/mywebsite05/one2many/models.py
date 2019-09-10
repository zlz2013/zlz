from django.db import models

# Create your models here.


class Publisher(models.Model):
    name=models.CharField('出版社名',max_length=50)

    def __str__(self):
        return '出版社名:'+self.name
class Book2(models.Model):
    title=models.CharField('书名',max_length=30)
    pub=models.ForeignKey(Publisher,on_delete=models.CASCADE)

    def __str__(self):
        return '书名:'+self.title