from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^add$',views.add_book_view),
    url(r'^$', views.homepage),
    url(r'^books$',views.books_view),
    url(r'^add2$',views.book_add2_view),
    url(r'^mod/(\d+)$',views.mod_book_view),
    url(r'^del/(\d+)$',views.del_book),
]
