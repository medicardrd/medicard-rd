from django.conf.urls import include, url
from . import views

extra_patterns = [
    # url(r'^reports/$', credit_views.report),
    # url(r'^reports/(?P<id>[0-9]+)/$', credit_views.report),
]


urlpatterns = [
    url(r'^$', views.inicio),
    url(r'^login/search/$', views.search, name='search'),
    url(r'^login/search/historial/(?P<user>\d*)$', views.historial, name='historial'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^medio/$', views.medio, name='medio'),
]