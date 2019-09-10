import html
import json

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from message.models import Message
from tools.login_check import login_check

from topic.models import Topic

from user.models import UserProfile

from tools.login_check import get_user_by_request


@login_check("POST")
def topics(request,author_id):
    #http://127.0.0.1:5000/<username>/topic/release
    if request.method=='POST':
        #发布博客
        json_str=request.body
        if not json_str:
            result={'code':302,'error':'Please POST data!!!'}
            return JsonResponse(result)
        json_obj = json.loads(json_str)
        title = json_obj.get('title')
        #带html标签样式的文章内容 [颜色...]
        content = json_obj.get('content')
        #纯文本的文章内容 用于截取简介
        content_text = json_obj.get('content_text')
        limit = json_obj.get('limit')
        category = json_obj.get('category')

        if not title:
            result={'code':303,'error':'Please give me title!!!'}
            return JsonResponse(result)
        #防止xss cross site script攻击
        title=html.escape(title)
        if not content:
            result={'code':304,'error':'Please give me content!!!'}
            return JsonResponse(result)
        if not content_text:
            result={'code':305,'error':'Please give me content_text!!!'}
            return JsonResponse(result)
        if not limit:
            result = {'code': 306, 'error': 'Please give me limit!!!'}
            return JsonResponse(result)
        if not category:
            result = {'code': 307, 'error': 'Please give me category!!!'}
            return JsonResponse(result)

        introduce=content_text[:30]

        if request.user.username!=author_id:
            result={'code': 308, 'error': 'Can not touch me!!!'}
            return JsonResponse(result)
        #创建数据
        try:
            Topic.objects.create(title=title,
                                 limit=limit,
                                 content=content,
                                 category=category,
                                 introduce=introduce,
                                 author_id=author_id)
        except Exception as e:
            print(e)
            result={'code': 309, 'error': 'Topic is busy!!!'}
            return JsonResponse(result)
        result={'code':200,'username':request.user.username}
        return JsonResponse(result)

    elif request.method=='GET':
        #获取author_id的文章
        #后端地址/v1/topics/<username>?category[tec/notec]
        #前端地址http://127.0.0.1:5000/<username>/topics

        #1,访问者 visitor
        #2,博主/作者 author
        #查找我们的大博主
        authors=UserProfile.objects.filter(username=author_id)
        if not authors:
            result={'code':310,'error':'The user is not existed!!'}
            return JsonResponse(result)

        author=authors[0]
        # print(author)
        # print(author.username)

        #查询我们的访问者
        visitor=get_user_by_request(request)
        # print(visitor)
        # print(visitor.username)
        visitor_username=None
        if visitor:
            visitor_username=visitor.username


        #判断查询字符串是否有t_id
        t_id=request.GET.get('t_id')
        print(type(t_id))
        print(t_id)
        if t_id:
            #查询用户的指定文章数据
            t_id=int(t_id)
            #是否为博主访问自己
            is_self=False
            if visitor_username == author_id:
                is_self=True
                # 博主访问自己的博客
                try:
                    author_topic=Topic.objects.get(id=t_id)
                except Exception as e:
                    result={'code':311,'error':'No topic!'}
                    return JsonResponse(result)
            else:
                #陌生人访问博主的博客
                try:
                    author_topic = Topic.objects.get(id=t_id,limit='public')
                except:
                    result={'code':312,'error':'No public topic!!'}
                    return JsonResponse(result)

            res=make_topic_res(author,author_topic,is_self)
            #http://127.0.0.1:5000/<username>/topics
            return JsonResponse(res)
        else:
            #查询用户的全部文章
            pass


        #判断是否有查询字符串【category】
        category=request.GET.get('category')
        if category in ['tec','no-tec']:
            if visitor_username == author.username:
                # 博主访问自己的博客
                author_topics = Topic.objects.filter(author_id=author.username,category=category)
            else:
                # 陌生的访问者， 访问author的博客
                author_topics = Topic.objects.filter(author_id=author.username, limit='public',category=category)
        else:
            if visitor_username==author.username:
                #博主访问自己的博客
                author_topics=Topic.objects.filter(author_id=author.username)
            else:
                #陌生的访问者， 访问author的博客
                author_topics=Topic.objects.filter(author_id=author.username,limit='public')
        res=make_topics_res(author,author_topics)
        return JsonResponse(res)

    elif request.method=='DELETE':
        #删除博客
        #查询字符串中包含topic_id
        topic_id=request.GET.get('topic_id')
        print(topic_id)
        if not topic_id:
            result={'code':201,'error':"未知错误！"}
            return JsonResponse(result)
        try:
            topic_obj=Topic.objects.get(topic_id)
            topic_obj.delete()
        except:
            print("删除失败!")
        pass



def make_topic_res(author,author_topic,is_self):
    #生成topic详情数据
    if is_self:
        #博主访问自己的博客
        #1,2,4,5,6,8,20
        #取出id大于当前ID数据的第一个 ->当前文章的下一篇
        next_topic=Topic.objects.filter(id__gt=author_topic.id,author=author).first()
        # 取出id小于当前ID数据的最后一个 ->当前文章的上一篇
        last_topic=Topic.objects.filter(id__lt=author_topic.id,author=author).last()
    else:
        #取出访客（陌生人）访问当前博客
        next_topic = Topic.objects.filter(id__gt=author_topic.id, author=author,limit='public').first()
        last_topic = Topic.objects.filter(id__lt=author_topic.id, author=author,limit='public').last()

    #生成下一个文章的ID和title
    if next_topic:
        next_id=next_topic.id
        next_title=next_topic.title
    else:
        next_id=None
        next_title=None
    #生成上一个文章的ID和title
    if last_topic:
        last_id=last_topic.id
        last_title=last_topic.title
    else:
        last_id=None
        last_title=None

    result={'code':200,'data':{}}
    result['data']['nickname']=author.nickname
    result['data']['title']=author_topic.title
    result['data']['category']=author_topic.category
    result['data']['created_time']=author_topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
    result['data']['content']=author_topic.content
    result['data']['introduce']=author_topic.introduce
    result['data']['author']=author.nickname
    result['data']['next_id']=next_id
    result['data']['next_title']=next_title
    result['data']['last_id']=last_id
    result['data']['last_title']=last_title

    ##留言&回复数据
    all_messages=Message.objects.filter(topic=author_topic).order_by('-created_time')
    #{1:[{'回复'},{'回复'}],}
    #[{'留言'}，{'留言'},]
    msg_dict={} #回复
    msg_list=[] #留言
    m_count=0
    for msg in all_messages:
        m_count+=1
        if msg.parent_message:
            #回复
            if msg.parent_message in msg_dict:
                msg_dict[msg.parent_message].append({'msg_id':msg.id,
                                                     'publisher':msg.publisher.nickname,
                                                     'publisher_avatar':str(msg.publisher.avatar),
                                                     'content':msg.content,
                                                     'created_time':msg.created_time.strftime('%Y-%m-%d %H:%M:%S')
                                                     })
            else:
                msg_dict[msg.parent_message]=[]
                msg_dict[msg.parent_message].append({'msg_id':msg.id,
                                                     'publisher':msg.publisher.nickname,
                                                     'publisher_avatar':str(msg.publisher.avatar),
                                                     'content':msg.content,
                                                     'created_time':msg.created_time.strftime('%Y-%m-%d %H:%M:%S')
                                                     })
        else:
            #留言
            msg_list.append({'id':msg.id,
                             'content':msg.content,
                             'publisher':msg.publisher.nickname,
                             'publisher_avatar':str(msg.publisher.avatar),
                             'created_time':msg.created_time.strftime('%Y-%m-%d %H:%M:%S'),
                             'reply':[]
                             })
    #关联 留言和对应的回复
    #msg_list--> [{留言相关的信息,'reply':[]}]
    for m in msg_list:
        if m['id'] in msg_dict:
            #证明当前的留言有回复信息
            m['reply']=msg_dict[m['id']]



    result['data']['messages']=msg_list
    result['data']['messages_count']=m_count

    print('11111111111111')
    print(result['data']['messages'])
    print('11111111111111')
    return result



def make_topics_res(author,author_topics):

    res={'code':200,'data':{}}
    topics_res=[]
    for topic in author_topics:
        d={}
        d['id']=topic.id
        d['title']=topic.title
        d['category']=topic.category
        d['created_time']=topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
        d['introduce']=topic.introduce
        d['author']=author.nickname
        topics_res.append(d)
    res['data']['topics']=topics_res
    res['data']['nickname']=author.nickname

    return res