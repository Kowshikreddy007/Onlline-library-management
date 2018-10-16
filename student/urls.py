from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.home, name='studenthome'),
	url(r'^signup/$', views.signup, name='studentsignup'),
	url(r'^signup/submit/$', views.signupsubmit, name='studentsignupsubmit'),
	url(r'^login/$', views.login, name='studentlogin'),
	url(r'^logout/$', views.logout, name='studentlogout'),
	url(r'^login/submit/$', views.loginsubmit, name='studentloginsubmit'),
]