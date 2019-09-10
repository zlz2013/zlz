from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index1_view(request):
    return HttpResponse('index/page1页')


def index2_view(request):
    return HttpResponse('index/page2页')

def index3_view(request):
    return HttpResponse('index/page3页')