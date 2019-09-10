from django.shortcuts import render
from django.http import HttpResponse,Http404
# from . import models  #不在使用自己的模型类
from django.contrib.auth import models  #使用django自带的用户系统的模型和他的User

# Create your views here.
def login_view(request):
    if 'user' in request.session:
        print('用户已登录')
    else:
        print("用户未登录")
    value=request.session.get('password','没有设置密码')
    print('密码是：',value)

    username=request.COOKIES.get('myname','')
    if request.method=='GET':
        return render(request,'user/login.html',locals())
    elif request.method=='POST':
        username=request.POST.get('username','')
        if username=='':
            name_error='请填写用户名!!!'
            return render(request,'user/login.html',locals())
        password=request.POST.get('password','')
        request.session['mypassword'] = password
        remember=request.POST.get('remember','0')

        #进行登录逻辑操作
        try:
            auser=models.User.objects.get(
                username=username
            )
            #若果得到用户，则要检查密码是否正确
            if auser.check_password(password) is False:
                password_error='密码不正确'
                return render(request,'user/login.html',locals())
        except:
            password_error='用户名或密码不正确!!!'
            return render(request,'user/login.html',locals())
        #如果能走到此处，说明用户名密码正确
        #在session里面标记用户是登录状态
        request.session['user']={
            'name':auser.username,
            'id':auser.id,
        }

        resp=HttpResponse("""提交成功:<a href='/'>
            返回主页</a>""")
        if remember=='1':
            resp.set_cookie('myname',username)
        else:
            resp.delete_cookie('myname')
        return resp



def logout_view(request):
        #退出登录
    if 'user' in request.session:
        del request.session['user']
    #返回主页
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect('/')


def reg_view(request):
    if request.method=="GET":
        return render(request,'user/reg.html',locals())
    elif request.method=='POST':
        username=request.POST.get('username','')
        if username=='':
            name_error='请填写用户名'
            return render(request,'user/reg.html',locals())
        password=request.POST.get('password','')
        password2=request.POST.get('password2','')
        if password!=password2:
            password2_error='两次密码不一致'
            return render(request,'user/reg.html',locals())
        #走到此处，数据合法,判断用户是否存在
        try:
            a_user=models.User.objects.get(username=username)
            name_error='用户名已存在'
            return render(request,'user/reg.html',locals())
        except:
            pass
        #添加用户数据，完成注册
        a_user=models.User.objects.create_superuser(
            username=username,
            password=password,
            email='',
        )
        html=username+"""注册成功<a href='/user/login'>
            进入登录</a>
        """
        return HttpResponse(html)


from . import forms
def reg2_view(request):
    if request.method=='GET':
        reg2=forms.Reg2()
        return render(request,'user/reg2.html',locals())
    elif request.method=='POST':
        #如何拿到表单数据？方法一
        #request.POST
        #方法二
        form=forms.Reg2(request.POST)
        if form.is_valid():
            html=str(form.cleaned_data)
            return HttpResponse(html)
        else:
            return HttpResponse('您提交的数据不合法')
