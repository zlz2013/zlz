from django.shortcuts import render
from django.http import HttpResponse,Http404
import os
from django.conf import settings
# Create your views here.

def index_view(request):
    return render(request,'index/index.html')


def upload_view(request):
    if request.method=='GET':
        return render(request,'index/upload_file.html',locals())
    elif request.method=='POST':
        #此时可以通过request.FILE来获取上传的文件
        a_file=request.FILES['myfile']
        #此处保存上传的文件到项目文件夹下mysite6/static/files文件夹内
        filename=os.path.join(settings.MEDIA_ROOT,a_file.name)
        with open(filename,'wb') as f:
            f.write(a_file.file.read())
            return HttpResponse('文件:'+a_file.name+' 上传成功')


