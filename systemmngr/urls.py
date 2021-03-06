from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='homepage'),

    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^loginout/$', views.loginout, name='loginout'),

    url(r'^user-list/$', views.user_list, name='user_list'),
    url(r'^user-add/$', views.user_add, name='user_add'),
    url(r'^user-edit/(?P<user_id>\d+)/$', views.user_edit, name='user_edit'),
    url(r'^user-delete/(?P<user_id>\d+)/$', views.user_delete, name='user_delete'),

    url(r'^get-current-role-req/(?P<user_id>\d+)/$', views.get_current_role_req, name='get_current_role'),
    url(r'^set-current-role-req/$', views.set_current_role_req_post, name='set_current_role'),

    url(r'^role-list/$', views.role_list, name='role_list'),
    url(r'^role-add/$', views.role_add, name='role_add'),
    url(r'^role-edit/(?P<role_id>\d+)/$', views.role_edit, name='role_edit'),
    url(r'^role-delete/(?P<role_id>\d+)/$', views.role_delete, name='role_delete'),
    
    url(r'^menu-role-list/$', views.menu_role_list, name='menu_role_list'),
    url(r'^get-tree-by-role-req/(?P<role_id>\d+)/$', views.get_tree_by_role_req, name='role_tree_list'),

    url(r'^user_role_list_req/(?P<role_id>\w+)/$', views.user_role_list_req, name='user_role_list'),
    url(r'^user_role_save_req/$', views.user_role_save_req_post, name='user_role_save'),
    
]
