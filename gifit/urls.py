from django.urls import path
from . views import RoleAPI,getUpdateDeleteRole
from .views import UserAPI,getUpdateDeleteUser,UserSignupAPI,UserSigin,Signup
from django.shortcuts import render
from django.conf.urls import url
from .views import FileUploadView


urlpatterns = [
	#url(r'^home', views.index, name='index'),
    url(r'^api/roles', RoleAPI.as_view()),
    url(r'^api/roles/(?P<id>[0-9]+)$',getUpdateDeleteRole.as_view()),

    url(r'^api/users', UserAPI.as_view()),
    url(r'^api/users/(?P<id>[0-9]+)$',getUpdateDeleteUser.as_view()),
    url(r'^api/signup',UserSignupAPI.as_view()),
    url(r'^api/signin',UserSigin.as_view()),
    url(r'^api/files',FileUploadView.as_view()),
    url(r'^api/check',Signup.as_view()),


]
