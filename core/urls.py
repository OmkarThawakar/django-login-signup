
from django.conf.urls import url
from . import views 
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [

    #home
    url(r'^signup/core/home',views.home , name='home'),
  
    #mcore/sign-up
    url(r'^signup/$', views.signup,name='signup'),

    #core/login
    url(r'login/$',auth_views.login,{'template_name':'core/login.html'},name='login'),

    #core/logout
    url(r'logout/$',auth_views.logout,name='logout'),
]
