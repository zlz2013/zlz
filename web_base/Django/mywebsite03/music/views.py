from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def page1_view(request):
    return HttpResponse('music/page1页')


def page2_view(request):
    return HttpResponse('music/page2页')

def page3_view(request):
    return HttpResponse('music/page3页')