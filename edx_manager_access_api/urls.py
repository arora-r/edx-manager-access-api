"""
URLs for edx_manager_access_api.
"""
from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^enable$', views.enable, name='enable'),
    url(r'^disable$', views.disable, name='disable')
]
