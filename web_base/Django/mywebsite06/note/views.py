from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.http import HttpResponseRedirect
from . import models
from user.models import User




#写一个装饰器函数,检查用户是否登录，如果没有登录，则直接跳转到登录界面
def check_login(fn):
    def wrap(request,*args,**kwargs):
        if 'user' not in request.session:
            return HttpResponseRedirect('/user/login')
        else:
            return fn(request,*args,**kwargs)
    return wrap

# Create your views here.
def add_view(request):
    #检查用户是否登录，如果没有登录，进入登录界面
    if 'user' not in request.session:
        return HttpResponseRedirect('/user/login')
    if request.method=='GET':
       return render(request,'note/add_note.html')
    elif request.method=='POST':
        #根据登录用户ID找到此用户
        try:
            a_user=User.objects.get(
                id=request.session['user']['id']
            )
        except:
            return HttpResponse('登录用户数据错误')
        title=request.POST.get('title','')
        content=request.POST.get('content','')
        #根据表单内容来创建记录
        models.Note.objects.create(
            title=title,
            content=content,
            user=a_user
        )
        return HttpResponseRedirect('/note/')


from django.core.paginator import  Paginator
@check_login
def list_view(request):
    #检查用户是否登录，如果没有登录，进入登录界面

    try:
        a_user_id=request.session['user']['id']
        a_user=User.objects.get(id=a_user_id)
    except:
        return HttpResponse('失败')
    notes=a_user.note_set.all() #获取当前用户的所有笔记
    # return render(request,'note/list_note.html',locals())

    paginator=Paginator(notes,5)
    print('分页前的数据个数：',paginator.count)
    print('当前页面的个数：',paginator.num_pages)
    print('page_range：',paginator.page_range)
    print('每页个数：',paginator.per_page)
    page_num=request.GET.get('page',1)
    page=paginator.page(page_num)

    return render(request,'note/list_note2.html',locals())


@check_login
def del_view(request,id):
    try:
        a_user_id = request.session['user']['id']
        a_user = User.objects.get(id=a_user_id)
    except:
        return HttpResponse('失败')
    #根据用户和ID找到对应的笔记
    a_note=a_user.note_set.get(id=id)
    a_note.delete()
    return HttpResponseRedirect('/note/')


def mod_view(request,id):
    try:
        a_user_id = request.session['user']['id']
        a_user = User.objects.get(id=a_user_id)
    except:
        return HttpResponse('失败')
    # 根据用户和ID找到对应的笔记
    a_note = a_user.note_set.get(id=id)

    if request.method=='GET':
        return render(request,'note/mod_note.html',locals())

    elif request.method=='POST':
        #从表单提取数据
        title=request.POST.get('title','')
        content=request.POST.get('content','')
        #修改对应的数据
        a_note.title=title
        a_note.content=content
        a_note.save()
        return HttpResponseRedirect('/note/')


