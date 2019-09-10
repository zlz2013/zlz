from django.contrib import admin

# Register your models here.
from . import models

class BookManager(admin.ModelAdmin):    #编写模型管理器类
    list_display = ['id','title','pub','price','market_price']
    list_display_links = ['id','title']
    list_filter = ['pub','title']

    search_fields = ['title','pub']
    list_editable = ['price','market_price']


class AuthorManager(admin.ModelAdmin):    #编写模型管理器类
    list_display = ['id','name','age','email']
    list_display_links = ['id','name']
    list_filter = ['name']

    search_fields = ['name']
    list_editable = ['email','age']

admin.site.register(models.Book,BookManager)
admin.site.register(models.Author,AuthorManager)
admin.site.register(models.Wife,AuthorManager)
