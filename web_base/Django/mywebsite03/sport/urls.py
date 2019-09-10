#file:music/urls.py

from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^page1$',views.sport1_view),
    url(r'^page2$',views.sport2_view),
    url(r'^page3$',views.sport3_view),

]