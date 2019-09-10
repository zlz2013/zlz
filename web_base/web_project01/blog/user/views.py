import hashlib
import json


from btoken.views import make_token

from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

from tools.login_check import login_check
from .models import *
# Create your views here.


@login_check('PUT')
def users(request,username=None):
    if request.method=='POST':
        #注册
        # print(request.body)
        json_str=request.body
        if not json_str:
            result={'code':202,'error':'Please POST data!!!'}
            return JsonResponse(result)
        #如果当前报错，请执行json_str.decode
        json_obj=json.loads(json_str)
        print(json_obj)
        username=json_obj.get('username')
        email=json_obj.get('email')
        password_1=json_obj.get('password_1')
        password_2=json_obj.get('password_2')

        if not username:
            result={'code':203,'error':'Please give me username!!!'}
            return JsonResponse(result)
        if not email:
            result={'code':204,'error':'Please give me email!!!'}
            return JsonResponse(result)
        if not password_1 or not password_2:
            result={'code':205,'error':'Please give me password!!!'}
            return JsonResponse(result)
        if password_1!=password_2:
            result={'code':206,'error':'Please give me right password!!!'}
            return JsonResponse(result)

        #检查用户名是否存在
        old_user=UserProfile.objects.filter(username=username)
        if old_user:
            result={'code':207,'error':'The username was used!!!'}
            return JsonResponse(result)

        #密码散列
        p_m=hashlib.sha256()
        p_m.update(password_1.encode())

        #创建用户
        try:
            UserProfile.objects.create(username=username,nickname=username,email=email,password=p_m.hexdigest())
        except Exception as e:
            print("------create error is %s"%e)
            result={'code':500,'error':'Sorry,server is busy!!!'}
            return JsonResponse(result)


        token=make_token(username)
        #token编码问题,bytes串不能json dumps所以需要使用decode方法
        result={'code': 200,'username':username,'data':{'token':token.decode()}}
        return JsonResponse(result)

    elif request.method=='GET':
        #获取数据
        if username:
            # 获取指定用户数据
            users = UserProfile.objects.filter(username=username)
            print(users[0].nickname)

            if not users:
                #当前用户不存在
                return JsonResponse({'code': 200, 'error': 'The user is not existed'})
            user=users[0]
            if request.GET.keys():
                #当前请求有查询字符串
                data={}
                for key in request.GET.keys():
                    if key=='password':
                        #如果查询密码，则continue
                        continue
                    #hasattr,第一个参数为对象，第二个参数为属性字符串，-->若对象有第二个参数的属性，则返回True，反之False
                    #gatattr,参数同hasattr，若对象含有第二个参数的属性，则返回对应属性的值，反之抛出异常：AttributeError
                    if hasattr(user,key):
                        if key=='avatar':
                            #avatar属性需要调用str方法  __str__
                            data[key]=str(getattr(user,key))
                        else:
                            data[key]=getattr(user,key)
                result={'code':200,'username':username,'data':data}
            else:
                #无查询字符串即获取制定用户所有数据
                result={'code':200,'username':username,'data':{'info':user.info,'sign':user.sign,'nickname':user.nickname,'avatar':str(user.avatar)}}
            return JsonResponse(result)

        else:
            #如果没有username
            #username nickname sign info email avatar
            #{'code':200,'data':{'info':user.info}}
            all_users = UserProfile.objects.all()
            print(all_users)
            result=[]
            for _user in all_users:
                d={}
                d['username']=_user.username
                d['nickname']=_user.nickname
                d['sign']=_user.sign
                d['info']=_user.info
                d['email']=_user.email
                d['avatar']=str(_user.avatar)
                result.append(d)
            return JsonResponse({'code':200,'data':result})

    elif request.method=='PUT':
        #前端访问地址 http://127.0.0.1:5000/<username>/change_info
        #后端地址 http://127.0.0.1:8000/v1/users/<username>
        #更新用户数据

        # user=check_token(request)
        user=request.user
        # if not user:
        #     result={'code':209,'error':'The PUT need token'}
        #     return JsonResponse(result)
        json_str=request.body
        json_obj=json.loads(json_str)
        nickname=json_obj.get('nickname')
        if not nickname:
            result={'code':210,'error':'The nickname can not be none!'}
            return JsonResponse(result)

        sign=json_obj.get('sign')
        if sign is None:
            result={'code':211,'error':'The sign not in json!'}
            return JsonResponse(result)

        info = json_obj.get('info')
        if info is None:
            result={'code':212,'error':'The info not in json!'}
            return JsonResponse(result)

        if user.username!=username:
            result = {'code': 213, 'error': 'This is wrong!'}
            return JsonResponse(result)

        #修改个人信息
        user.sign=sign
        user.info=info
        user.nickname=nickname
        user.save()
        result = {'code': 200, 'username': username}
        return JsonResponse(result)

@login_check('POST')
def user_avatar(request,username):
    #当前只开放post请求
    if request.method!='POST':
        result={'code':214,'error':'Please use POST!!!'}
        return JsonResponse(result)
    #获取用户
    user=request.user
    if user.username!=username:
        #异常请求
        result={'code':215,'error':'You are wrong!!!'}
        return JsonResponse(result)

    #获取上传图片，上传方式是表单提交
    avatar=request.FILES.get('avatar')
    if not avatar:
        result = {'code': 216, 'error': 'Please give me avatar!!!'}
        return JsonResponse(result)

    #更新
    user.avatar=avatar
    user.save()
    result={'code': 200, 'username': username}
    return JsonResponse(result)


