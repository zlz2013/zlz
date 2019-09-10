from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def set_cookie(request):
    resp=HttpResponse('OK')
    resp.set_cookie('aaa','123456')
    return resp


def get_cookie(request):
    v=request.COOKIES['aaa']
    print('v=',v)
    dic=request.COOKIES
    s=str(dic)
    return HttpResponse(s)