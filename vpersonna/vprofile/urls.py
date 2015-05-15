from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name="dashboard"),
    url(r'^stats$', views.stats, name="stats"),
    url(r'^manage$', views.manage, name="manage"),
    #url(r'^manage2$', views.manage2, name="manage2"),
    url(r'^rule_edit$', views.rule_edit, name="rule_edit"),
    url(r'^rule_update/(?P<pk>[0-9]+)$', views.rule_update, name='rule_update'),
    url(r'^rule_delete/(?P<pk>[0-9]+)$', views.rule_delete, name='rule_delete'),
    url(r'^offers$', views.offers, name="offers"),
    url(r'^transactions$', views.transactions, name="transactions"),
    url(r'^date$', views.stats_date, name="stats_date"),
]

