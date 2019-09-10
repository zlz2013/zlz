from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index_view(request):
    return HttpResponse('news/page1页')


def news2_view(request):
    return HttpResponse('news/page2页')

def news3_view(request):
    return HttpResponse('news/page3页')