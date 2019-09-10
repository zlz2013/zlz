from django.shortcuts import render

# Create your views here.
from . import models
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def add_book_view(request):
    if request.method=='GET':
        btitle=request.GET.get('title','No Name')
        bpub=request.GET.get('pub','')
        #创建一条记录
        #方法一
        # models.Book.objects.create(
        #     title=btitle,
        #     pub=bpub,
        # )
        #方法二
        book=models.Book()
        book.title=btitle
        book.pub=bpub
        book.price=99.9
        # import datetime
        # book.pub_date=datetime.datetime(2008,1,1).date()
        book.pub_date='2019-7-15'
        book.save() #执行SQL语句

        print(book)
        return HttpResponse("添加成功")


def books_view(request):
    books=models.Book.objects.all()
    # books=models.Book.objects.filter(pub='清华大学出版社',title='python3')
    # books=models.Book.objects.filter(price__exact='99.90')

    return render(request,'bookstore/books.html',locals())

def book_add2_view(request):
    if request.method=='GET':
        return render(request,'bookstore/bookinfo.html')
    elif request.method=='POST':
        id=request.POST.get('id','')
        title=request.POST.get('title','')
        pub=request.POST.get('pub','')
        price=request.POST.get('price','0.0')
        market_price=request.POST.get('market_price','0.0')

        try:
            books = models.Book.objects.get(id=id)
            abook=models.Book.objects.create(
                title=title,
                pub=pub,
                price=price,
                market_price=market_price

            )
            return HttpResponseRedirect('/bookstore/books')
        except:
            return HttpResponse('添加失败')

def mod_book_view(request,id):
    # 先根据book_id 找到对应的一本书
    try:
        abook = models.Book.objects.get(id=id)
    except:
        return HttpResponse("没有找到ID为" + id + "的图书信息")

    if request.method == 'GET':
        return render(request, "bookstore/mod_price.html", locals())
    elif request.method == 'POST':
        try:
            m_price = request.POST.get('market_price', '0.0')
            abook.market_price = m_price
            abook.save()  # 提交修改
            return HttpResponse("修改成功")
        except:
            return HttpResponse("修改失败")

def del_book(request, book_id):
    try:
        abook = models.Book.objects.get(id=book_id)
        abook.delete()
        return HttpResponseRedirect('/bookstore/books')
    except:
        return HttpResponse("没有找到ID为" + book_id + "的图书信息,删除失败")


def homepage(request):
    return render(request, 'bookstore/index.html')