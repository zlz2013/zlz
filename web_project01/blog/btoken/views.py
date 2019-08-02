import json
import jwt
import time
import hashlib
from django.http import JsonResponse
from django.shortcuts import render
from user.models import UserProfile
# Create your views here.



def tokens(request):
    """
    创建token-->登录
    :param request:
    :return:
    """
    #前端访问http://127.0.0.1:5000/login

    if not request.method=='POST':
        result={'code':102,"error":'Plaase use post'}
        return JsonResponse(result)


    json_str = request.body
    if not json_str:
        result = {'code': 103, 'error': 'Please give me json!!!'}
        return JsonResponse(result)
    # 如果当前报错，请执行json_str.decode
    json_obj = json.loads(json_str)
    print(json_obj)
    username = json_obj.get('username')
    password = json_obj.get('password')
    print(username,password)

    if not username:
        result={'code': 104, 'error': 'Please give me username!!!'}
        return JsonResponse(result)

    if not password:
        result={'code': 105, 'error': 'Please give me password!!!'}
        return JsonResponse(result)


    users = UserProfile.objects.filter(username=username)
    print(users[0])

    print(users[0].password)

    if not users:
        result={'code': 106, 'error': 'The username or password is wrong!!!'}
        return JsonResponse(result)

    #生成密码hash
    p_m = hashlib.sha256()
    p_m.update(password.encode())
    if users[0].password!=p_m.hexdigest():
        result = {'code': 107, 'error': 'The username or password is wrong!!!'}
        return JsonResponse(result)

    #生成token
    token = make_token(username)
    # token编码问题,bytes串不能json dumps所以需要使用decode方法
    result = {'code': 200, 'username': username, 'data': {'token': token.decode()}}

    return JsonResponse(result)






def make_token(username,expire=3600*24):
    #生成token
    key='123abc'
    now_t=time.time()
    data={'username':username,'exp':int(now_t+expire)}
    return jwt.encode(data,key,algorithm='HS256')

def check_token(request):
    token=request.META.get('HTTP_AUTHORIZATION')
    if not token:
        return None
    key = '123abc'

    try:
        res=jwt.decode(token,key)
    except Exception as e:
        print('check_token error is %s'%e)
        return None
    username=res['username']
    users=UserProfile.objects.filter(username=username)
    return users[0]

