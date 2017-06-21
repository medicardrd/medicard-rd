from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.inicio),
    url(r'^login/search/$', views.search, name='search'),
    url(r'^login/search/historial$', views.historial, name='historial'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^medio/$', views.medio, name='medio'),
]