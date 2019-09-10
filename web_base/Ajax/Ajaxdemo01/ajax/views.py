import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse  导包快捷键alt+回车
from ajax.models import Users
from . import models

def create_view(request):
    return render(request,'01-createxhr.html')

def server02_view(request):
    return HttpResponse('这是server02的响应内容')

def ajaxget_view(request):
    return render(request,'02-ajax-get.html')

def getparams_view(request):
    return render(request,'03-ajax-get-params.html')

def server03_view(request):
    #1.接收前端传递过来的两个参数
    name=request.GET['name']
    age=request.GET['age']
    #2.响应数据给前端
    s='姓名:%s,年龄:%s'%(name,age)
    return HttpResponse(s)


def register_view(request):
    return render(request,'04-register.html')

def checkuname_view(request):
    #1.接收前端传递过来的参数-uname
    uname=request.GET['uname']

    #2.判断uname在Users实体中是否存在【查询操作】
    users=Users.objects.filter(uname=uname)
    #3.根据查询的结果给出响应
    if users:
        return HttpResponse('1')
    return HttpResponse('0')

def reguser_view(request):
    #1.接收前端传递的数据
    uname = request.GET['uname']
    upwd = request.GET['upwd']
    uemail = request.GET['uemail']
    nickname = request.GET['nickname']
    #2.通过实体类实现增加操作(通过异常处理增加失败的问题)
    try:
        Users.objects.create(uname=uname,upwd=upwd,uemail=uemail,nickname=nickname)
        return HttpResponse('1')
    except Exception as ex:
        print(ex)
        return HttpResponse('0')

def post_view(request):
    return render(request,'05-post.html')


def server05_view(request):
    uname=request.POST['uname']
    upwd=request.POST['upwd']
    msg='用户名:%s,密码:%s'%(uname,upwd)
    return HttpResponse(msg)

def regpost_view(request):
    # 1.接收前端传递的数据
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    uemail = request.POST['uemail']
    nickname = request.POST['nickname']
    # 2.通过实体类实现增加操作(通过异常处理增加失败的问题)
    try:
        Users.objects.create(uname=uname, upwd=upwd, uemail=uemail, nickname=nickname)
        return HttpResponse('1')
    except Exception as ex:
        print(ex)
        return HttpResponse('0')


def users_view(request):
    return render(request,'06-ajax-users.html')

def server06_view(request):
    users=Users.objects.all()
    msg=''
    for u in users:
        msg+='%s_%s_%s_%s_%s|'%(u.id,u.uname,u.upwd,u.uemail,u.nickname)
    msg=msg[0:-1]
    return HttpResponse(msg)



def json_view(request):
    return render(request,'07-json.html')

def jsonserver_view(request):
    # #1.使用字典表示JSON数据
    # dic={
    #     'course':'ajax',
    #     'duration':3,
    #     'place':'北京',
    # }
    # #2.将dic通过json.dumps转换成JSON格式的字符串
    # jsonStr=json.dumps(dic)
    # return HttpResponse(jsonStr)
    list1=[
        {
            'course': 'ajax',
            'duration': 3,
            'place': '北京',
        },
        {
            'course': 'django',
            'duration': 3,
            'place': '上海',
        }
    ]
    jsonList=json.dumps(list1)
    return HttpResponse(jsonList)


def jsonusers_view(request):
    users=Users.objects.all()
    # jsonUser=json.dumps(users)  #queryset不支持json
    jsonUsers=serializers.serialize("json",users)

    return HttpResponse(jsonUsers)

def server10_view(request):
    return render(request,'10-users.html')


def front_view(request):
    return render(request,"11-front-json.html")

def serverjosn_view(request):
    jsonStr='{"uname":"wangwc","uage":30,"ugender":"男"}'
    #通过json.loads()将jsonStr转换为Python字典
    dic=json.loads(jsonStr)
    s='姓名：%s,年龄：%s,性别：%s'%(dic['uname'],dic['uage'],dic['ugender'])
    return HttpResponse(s)

def regjson_view(request):
    return render(request,'12-register.html')

def server12_view(request):
    params=request.GET['params']
    #将params转换上python字典
    dic=json.loads(params)
    print(dic)
    try:
        Users.objects.create(uname=dic['uname'],upwd=dic['upwd'],uemail=dic['uemail'],nickname=dic['nickname'])
        return HttpResponse('注册成功')
    except Exception as ex:
        print(ex)
        return HttpResponse('注册失败')

def head_view(request):
    return render(request,'13-head.html')


def index_view(request):
    return render(request,'13-index.html')

def jqget_view(request):
    return render(request,'14-jq-get.html')

def search_view(request):
    return render(request,'15-search.html')

def server15_view(request):
    #1.接收前端传递过来的参数 - kw
    kw=request.GET['kw']
    #2.查询Users实体中uname列中包含kw的信息
    users=Users.objects.filter(uname__contains=kw)
    #3.把uname封装成列表，在转换成JSON串 响应
    ulist=[]
    if users:
        for u in users:
            ulist.append(u.uname)
    return HttpResponse(json.dumps(ulist))

def jqajax_view(request):
    return render(request,'16-jq-ajax.html')