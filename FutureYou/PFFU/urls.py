from django.conf.urls import url,include
from django.contrib import admin
import PFFU.views
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static


app_name = 'PFFU'

urlpatterns = [
    url(r'^login', PFFU.views.search, name='login'),
    url(r'^signup', PFFU.views.register, name='signup'),
    #url(r'^test2', PFFU.views.current_profile, name='test2'),
    #(r'^loginVerify/$', PFFU.views.loginVerify, name='loginVerify'),
    url(r'^index', PFFU.views.index, name='index'),
    url(r'^portfolio', PFFU.views.portfolio, name='portfolio'),
    url(r'^current_profile', PFFU.views.current_profile, name='current_profile'),
    url(r'^profile', PFFU.views.profile, name='profile'),
    url(r'^workshops', PFFU.views.workshops, name='workshops'),
    url(r'^understanding_yourself', PFFU.views.understanding_yourself, name='understanding_yourself'),
    url(r'^uy_yes', PFFU.views.uy_yes, name='uy_yes'),
    url(r'^research_employer', PFFU.views.research_employer, name='research_employer'),
    url(r'^interview_skill', PFFU.views.interview_skill, name='interview_skill'),
    url(r'^career_goal', PFFU.views.career_goal, name='career_goal')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)