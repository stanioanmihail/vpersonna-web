from django.conf.urls import include, url
from . import views

urlpatterns = [
    #auth views
    url(r'^$', views.home, name="home"),
    url(r'^login$', views.auth_method_login, name="login"),
    url(r'^logout$', views.auth_method_logout, name="logout"),
    url(r'^change_passwd$', views.change_password, name="change_passwd"),

    #admin pages
    #clients management
    url(r'^client$', views.client_management, name="client_mng"),
    url(r'^client_update/(?P<pk>[0-9]+)$', views.update_client_admin_method, name="client_update"),
    url(r'^client_delete/(?P<pk>[0-9]+)$', views.delete_client_admin_method, name="client_delete"),
    url(r'^new_client$', views.new_client_admin_method, name="new_client"),

    #news post management
    url(r'^news$', views.news_management, name="news_mng"),
    url(r'^news_update/(?P<pk>[0-9]+)$', views.update_post_admin_method, name="news_update"),
    url(r'^news_delete/(?P<pk>[0-9]+)$', views.delete_post_admin_method, name="news_delete"),
    url(r'^new_post$', views.new_post_admin_method, name="new_post"),

    #ip allocation per client management
    url(r'^ip_alloc_mng$', views.ipalloc_management, name="ip_alloc_mng"),
    url(r'^ipalloc_update/(?P<pk>[0-9]+)$', views.update_ipalloc_admin_method, name="ipalloc_update"),
    url(r'^ipalloc_delete/(?P<pk>[0-9]+)$', views.delete_ipalloc_admin_method, name="ipalloc_delete"),
    url(r'^new_alloc$', views.new_ipalloc_admin_method, name="new_ip_alloc"),

    #regular user pages
    #dashboard and global statistics
    url(r'^dashboard$', views.dashboard, name="dashboard"),

    #advanced statistics 
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
    url(r'^activity_logs$', views.activity, name="activity"),


]

