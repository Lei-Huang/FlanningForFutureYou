from django.conf.urls import url,include
from django.contrib import admin
import PFFU.views
admin.autodiscover()

urlpatterns = [
    url(r'^login/$', PFFU.views.login, name='login'),
    url(r'^signup/$', PFFU.views.regist, name='signup'),
    url(r'^loginVerify/$', PFFU.views.loginVerify, name='loginVerify'),
    url(r'^index/$', PFFU.views.index, name='index'),
]