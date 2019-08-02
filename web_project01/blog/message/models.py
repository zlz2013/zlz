from django.db import models
from topic.models import Topic
# Create your models here.
from user.models import UserProfile


class Message(models.Model):
    #topic外键
    topic = models.ForeignKey(Topic)
    #UserProfile外键
    publisher = models.ForeignKey(UserProfile)
    content = models.CharField('内容',max_length=90)
    created_time = models.DateField(auto_now_add=True)
    #父级message的ID，默认为0 0>留言，非0>回复
    parent_message = models.IntegerField(default=0)



    

    class Meta:

        db_table = 'message'