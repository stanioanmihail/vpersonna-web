from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^(?P<client_id>\d+)/dashboard$', views.dashboard, name="dashboard"),
    url(r'^(?P<client_id>\d+)/stats$', views.stats, name="stats"),
    url(r'^(?P<client_id>\d+)/manage$', views.manage, name="manage"),
    url(r'^(?P<client_id>\d+)/rule_edit$', views.rule_edit, name="rule_edit"),
    url(r'^(?P<client_id>\d+)/rule_update/(?P<pk>[0-9]+)$', views.rule_update, name='rule_update'),
    url(r'^(?P<client_id>\d+)/rule_delete/(?P<pk>[0-9]+)$', views.rule_delete, name='rule_delete'),
    url(r'^(?P<client_id>\d+)/offers$', views.offers, name="offers"),
    url(r'^(?P<client_id>\d+)/transactions$', views.transactions, name="transactions"),
    url(r'^(?P<client_id>\d+)/date$', views.stats_date, name="stats_date"),
]

