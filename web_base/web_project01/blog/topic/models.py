from django.db import models

# Create your models here.
from user.models import UserProfile


class Topic(models.Model):
    title = models.CharField("文章主题", max_length=50)
    #'tec'--技术类  'no-tec'--非技术类
    category = models.CharField("博客的分类", max_length=20)
    # 'public'--公开的  'private'--私有的
    limit = models.CharField('权限',max_length=10)
    introduce = models.CharField('博客简介', max_length=90)
    content = models.TextField('博客内容')
    created_time = models.DateField('博客的创建时间', auto_now_add=True)
    modified_time = models.DateField('博客的修改时间', auto_now=True)
    author = models.ForeignKey(UserProfile)

    def __str__(self):
        return "博客主题:" + self.title

    class Meta:

        db_table = 'topic'