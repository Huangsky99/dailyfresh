from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^lists/$', views.lists),
    url(r'^cart/$', views.cart),
    url(r'^detail/$', views.detail),
    url(r'^order/$', views.order),
    url(r'^user_info/$', views.user_info),
    url(r'^user_order/$', views.user_order),
    url(r'^user_site/$', views.user_site),
]