# from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    # url('', views.index),
    # url('map', views.map_views)
    path('', views.index),
    path('map', views.map_views)
    # path('download.html', views.download),
    # path('login.html', views.login),
    # path('<int:id>.html', views.model_index)
]
