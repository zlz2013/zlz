from django.conf.urls import url


from . import views
urlpatterns = [
    #1.演示创建xhr
    url(r'^01-createxhr/$', views.create_view),
    #2.演示使用ajax发送get请求的步骤
    url(r'^02-server/$',views.server02_view),
    url(r'^02-ajax-get/$',views.ajaxget_view),
    #3.演示使用ajax发送get请求并附带参数
    url(r'^03-ajax-get-params/$',views.getparams_view),
    url(r'^03-server/$',views.server03_view),
    #4.使用ajax完成注册操作
    url(r'^04-register/$',views.register_view),
    url(r'^04-checkuname/$',views.checkuname_view),
    url(r'^04-reguser/$',views.reguser_view),
    url(r'^04-regpost/$',views.regpost_view),

    #5.使用ajax发送post请求
    url(r'^05-ajax-post/$',views.post_view),
    url(r'^05-server/$',views.server05_view),

    #6.使用ajax读取数据库数据
    url(r'^06-ajax-users/$',views.users_view),
    url(r'^06-server/$',views.server06_view),

    #7.在前端中处理json格式字符串
    url(r'^07-json/$',views.json_view),

    #8.在服务器端中处理JSON字符串
    url(r'^08-json-server/$',views.jsonserver_view),

    #9.在服务器端中，读取Users表中的数据在转换成JSON串
    url(r'^09-json-users/$',views.jsonusers_view),

    url(r'^10-server/$',views.server10_view),

    #11.前端中将js对象转换成JSON串
    url(r'^11-front-json/$',views.front_view),
    url(r'^11-server-json/$',views.serverjosn_view),


    #12.使用ajax完成注册操作
    url(r'^12-register-json/$',views.regjson_view),
    url(r'^12-server/$',views.server12_view),

    #13.演示jQuery中的$obj.load()的作用
    url(r'^13-head/$',views.head_view),
    url(r'^13-index/$',views.index_view),

    #14.演示jQuery中的$.get()的作用
    url(r'^14-jq-get/$',views.jqget_view),

    #15.通过$.get()完成搜索建议
    url(r'^15-search/$',views.search_view),
    url(r'^15-server/$',views.server15_view),

    #16.通过$.ajax()完成自定义的ajax请求
    url(r'^16-jq-ajax/$',views.jqajax_view),
]