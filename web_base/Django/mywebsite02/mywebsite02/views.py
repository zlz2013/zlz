

from django.http import HttpResponse

def sum_view(request):
    if request.method=='GET':
        start=request.GET.get('start','0')
        stop=request.GET.get('stop')
        step=request.GET.get('step','1')
        start,stop,step=int(start),int(stop),int(step)
        result=sum(range(start,stop,step))
    return HttpResponse('结果:%d'%result)

html="""
<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta charset="UTF-8">
    <title>form表单</title>
</head>
<body>
  <!--网页表单-->
  <!--form负责提交数据给服务器-->
  <!--action制定数据提交地址-->
  <!--method制定数据的提交方式，默认为get-->
  <!--enctype制定数据的编码方式，默认转字符串，拼接在URL后面（urlencode）,如果涉及到二进制数据（图片，音视频），
  必须设置为post，同事设置编码类型为multipart/form-data.-->
    <form action="/test" method="post"  >
        <p>
            用户姓名：<input type="text" name="username" placeholder="用户名由数字和字母组成" maxlength="10">
        </p>
        <p>
            用户密码：<input type="password" name="userpwd" placeholder="请输入密码" maxlength="10" minlength="6">
        </p>
        <p>
            用户性别：<input type="radio" name="sex" value="boy" id="boy">
            <label for="boy">男</label>
            <input type="radio" name="sex" value="girl" checked id="girl">
            <label for="girl">女</label>
        </p>
        <p>
            兴趣爱好:
            <!--label for id 用来实现文本与控件的绑定，
            将label标签属性for取值为对应控件的ID值-->
            <input type="checkbox" name="hobby" id="1" value="smoke">
            <label for="1">抽烟</label>
            <input type="checkbox" name="hobby" id="2" value="masage">
            <label for="2">喝酒</label>
            <input type="checkbox" name="hobby" id="3" value="dubo">
            <label for="3">保健</label>
        </p>
        <!--隐藏域（了解）：将一些服务器端需要，
        但是用户不需要了解数据提交过去，对于用户不可见-->
        <input type="hidden" name="uid" value="001" >
        <!--下拉菜单-->
        <select name="city" id="">
            <option value="beijing">北京</option>
            <option value="shanghai">上海</option>
            <option value="guangzhou">广州</option>
            <option value="shenzhen" selected>深圳</option>
        </select>
        <!--功能按钮-->
        <!--1.提交按钮,点击时提交数据到后台，
        可以设置value属性，表示按钮显示文本-->
        <input type="submit" value="注册">
        <!--2.重置按钮，点击时将表单还原至初始状态-->
        <input type="reset" value="重填">
        <!--3.普通按钮，需要自定义点击处理-->
        <!--文件选择框，涉及二进制数据提交必须使用post方式
        同事设置编码类型为multipart/form-data-->
        用户头像：<input type="file" name="uimg" formenctype="multipart/form-data">
        <input type="button" value="妹子">
        <!--button标签表示按钮，标签内容即为按钮显示文本书写在form中
        书写在form中，相当于submit提交按钮
        书写在form外，相当于普通按钮，需要自定义点击操作-->


        <button>form内</button>
    </form>
    <button>form外</button>
</body>
</html>

"""
from django.template import loader
from django.shortcuts import render
def test_post_view(request):
    if request.method=="GET":
        return HttpResponse(html)
    elif request.method=='POST':
        value=request.POST['username']
        dic=dict(request.POST)
        return HttpResponse('username='+value+str(dic))

def test1_view(request):
    #t绑定模板对象
    t=loader.get_template('01_page.html')
    #用模板生成html
    html=t.render()
    #返回给浏览器
    return HttpResponse(html)

class Dog:
    def show_info(self):
        return '二哈'
def test2_view(request):
    myvar=999
    mystr='Hello World'
    mylist=['北京','上海','深圳']
    # mylist=[]
    person={'name':'tedu','age':19}
    # person={
    #     'name':'tedu',
    #     'age':19,
    #     'myvar':myvar,
    #     'mystr':'hello world',
    #     'mylist':['北京','上海','深圳'],
    #
    # }
    def myfun1():
        return '函数结果!!!'
    #myfun1=lambda : '函数结果!!!'
    dog1=Dog()

    money=9999999
    return render(request,'01_page.html',locals())


def page0_view(request):
    return render(request,'mybase.html')

def page1_view(request):
    return render(request,'page1.html')

def page2_view(request):
    return render(request,'page2.html')

def page3_view(request,n):
    return render(request,'page3.html',locals())

def pagen_view(request,n):
    return render(request,'pagen.html',locals())