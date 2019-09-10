from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sport1_view(request):
    return HttpResponse('sport/page1页')


def sport2_view(request):
    return HttpResponse('sport/page2页')

def sport3_view(request):
    return HttpResponse('sport/page3页')