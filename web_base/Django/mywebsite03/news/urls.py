#file:music/urls.py

from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^index$',views.index_view),
    url(r'^page2$',views.news2_view),
    url(r'^page3$',views.news3_view),

]