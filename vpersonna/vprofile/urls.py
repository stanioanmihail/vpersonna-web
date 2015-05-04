from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name="dashboard"),
    url(r'^stats$', views.stats, name="stats"),
    url(r'^manage$', views.manage, name="manage"),
    url(r'^offers$', views.offers, name="offers"),
    url(r'^transactions$', views.transactions, name="transactions"),
    url(r'^date$', views.stats_date, name="stats_date"),
]

