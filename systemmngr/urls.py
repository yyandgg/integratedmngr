from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='homepage'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^loginout/$', views.loginout, name='loginout'),
    url(r'^role-list/$', views.role_list, name='role_list'),
    url(r'^role-add/$', views.role_add, name='role_add'),
    url(r'^role-edit/(?P<role_id>)/$', views.role_edit, name='role_edit'),
    url(r'^role-delete/(?P<role_id>)/$', views.role_delete, name='role_delete'),
    
]
