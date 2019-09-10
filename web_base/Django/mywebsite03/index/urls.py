#file:music/urls.py

from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^page1$',views.index1_view),
    url(r'^page2$',views.index2_view),
    url(r'^page3$',views.index3_view),

]