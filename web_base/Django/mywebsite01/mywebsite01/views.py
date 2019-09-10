

from django.http import HttpResponse

def page1_view(request):
    html='欢迎来到第一个页面'
    html+='<a href="http://www.baidu.com">百度</a><br>'
    html+='<a href="/">返回首页</a><br>'
    html += '<a href="/page2">返回第二页</a>'
    return HttpResponse(html)

def index_view(request):
    html="欢迎来到达内!"
    html+='跳转到第一页<a href="/page1">第一页</a>'
    return HttpResponse(html)


def page2_view(request):
    html='欢迎来到第二个页面'
    html+='<a href="http://www.baidu.com">百度</a><br>'
    html+='<a href="/">返回首页</a><br>'
    html+='<a href="/page1">返回第一页</a>'
    return HttpResponse(html)


def year_view(request,y):
    html='URL中的年份是:'+y
    return HttpResponse(html)

def cal_view(request,num1,op,num2):
    num1=int(num1)
    num2=int(num2)
    s=0
    if op=='add':
        s=num1+num2
    elif op=="-":
        s=num1-num2
    elif op=='*':
        s=num1*num2
    html='运算的结果为:%d %s %d = %d'%(num1,op,num2,s)
    return HttpResponse(html)


def date_view(request,y,m,d):
    # y,m,d是年月日
    html=y+'年'+m+'月'+d+'日'
    return HttpResponse(html)


def show_info(request):
    html='request.path='+request.path
    if request.method=='GET':
        html+='<h6>您正在进行GET请求<h6>'
    elif request.method=='POST':
        html += '<h6>您正在进行POST请求<h6>'
    html+='<h6>您的IP地址是:<h6>'+request.META['REMOTE_ADDR']
    # html+='<br>'+str(request.META)
    return HttpResponse(html)

def page_view(request):
    html=''
    if request.method=='GET':
        dic=dict(request.GET)
        s=str(dic)
        html+='GET请求:'+s
        a=request.GET.getlist('a',"没有值!!!")
        b=request.GET.get('b',"没有值!!!")
        html+='<br> a='+str(a)
        html+='<br> a='+b
    elif request.method=='POET':
        pass
    return HttpResponse(html)

def sum_view(request):
    html = ''
    if request.method == 'GET':
        dic = dict(request.GET)
        s = str(dic)
        html += '输出的结果为:'
        a = request.GET.get('start', "0")
        a=int(a)
        b = request.GET.get('stop', "没有值!!!")
        b = int(b)
        c = request.GET.get('step', "没有值!!!")
        c = int(c)
        html += str(sum(range(a,b,c)))
    elif request.method == 'POET':
        pass
    return HttpResponse(html)