from django.conf.urls import include, url
from . import views

urlpatterns = [
    #auth views
    url(r'^$', views.home, name="home"),
    url(r'^login$', views.auth_method_login, name="login"),
    url(r'^logout$', views.auth_method_logout, name="logout"),
    url(r'^new_client$', views.new_client_admin_method, name="new_client"),

    #dashboard and statistics
    url(r'^dashboard$', views.dashboard, name="dashboard"),
    url(r'^stats$', views.stats, name="stats"),
    url(r'^date$', views.stats_date, name="stats_date"),

    #resource management
    url(r'^manage$', views.manage, name="manage"),
    url(r'^rule_edit$', views.rule_edit, name="rule_edit"),
    url(r'^rule_update/(?P<pk>[0-9]+)$', views.rule_update, name='rule_update'),
    url(r'^rule_delete/(?P<pk>[0-9]+)$', views.rule_delete, name='rule_delete'),

    #offers
    url(r'^offers$', views.offers, name="offers"),

    #transaction & activities
    url(r'^transactions$', views.transactions, name="transactions"),

]

