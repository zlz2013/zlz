"""mywebsite_bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from index import views as index_view
from django.conf.urls import include  # <-- 新导入 include 函数

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bookstore/', include('bookstore.urls')),
    url(r'^cs/',include('cookie_session.urls')),
    url(r'^user/',include('user.urls')),
    url(r'^note/',include('note.urls')),
    url(r'^$',index_view.index_view),
    url(r'^upload',index_view.upload_view),
]

