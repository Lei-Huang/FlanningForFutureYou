from django.conf.urls import url,include
from django.contrib import admin
import PFFU.views
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static


app_name = 'PFFU'

urlpatterns = [
    url(r'^login', PFFU.views.search, name='login'),
    url(r'^signup', PFFU.views.regist, name='signup'),
    #(r'^loginVerify/$', PFFU.views.loginVerify, name='loginVerify'),
    #url(r'^index/$', PFFU.views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)