from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='homepage'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^loginout/$', views.loginout, name='loginout'),
]
