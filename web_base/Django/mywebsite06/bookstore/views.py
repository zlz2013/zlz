from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'index.html')

from django.http import HttpResponse
from . import models
def new_book(request):
    if request.method == 'GET':
        return render(request, 'new_book.html')
    elif request.method == 'POST':
        title = request.POST.get('title', '')
        pub= request.POST.get('pub', '')
        price = request.POST.get('price', '')
        market_price = request.POST.get('market_price', '')
        # 用Book.object管理器的create方法来创建新书
        abook = models.Book.objects.create(title=title,
                                           price=price,
                                           market_price=market_price,
                                           pub=pub)
        print('添加新书,成功添加新书:', abook.title)
        return HttpResponse('<a href="/bookstore">添加新书成功，点我跳转到首页</a>')

def list_books(request):
    books = models.Book.objects.all()

    resp=render(request, 'book_list.html', locals())
    resp.set_cookie('myvar',100)
    return resp


def mod_book_info(request, book_id):
    # 先根据book_id 找到对应的一本书
    try:
        abook = models.Book.objects.get(id=book_id)
    except:
        return HttpResponse("没有找到ID为" + book_id + "的图书信息")

    if request.method == 'GET':
        return render(request, "mod_price.html", locals())
    elif request.method == 'POST':
        try:
            m_price = request.POST.get('market_price', '0.0')
            abook.market_price = m_price
            abook.save()  # 提交修改
            return HttpResponse("修改成功")
        except:
            return HttpResponse("修改失败")


from django.http import HttpResponseRedirect  # 改入 HttpResponseRedirect模块用于 重定向url
def del_book(request, book_id):
    try:
        abook = models.Book.objects.get(id=book_id)
        abook.delete()
        return HttpResponseRedirect('/bookstore/list_all')
    except:
        return HttpResponse("没有找到ID为" + book_id + "的图书信息,删除失败")


