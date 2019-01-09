from django.conf.urls import url, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib import admin
from reg.views import *

app_name='reg'

urlpatterns = [

	url(r'^registeroff/$', offLineRegister, name="kaleidoscope"),  # from register to registeroff
	url(r'main/$',intro,name='mainPage'),
	url(r'^details/$',details,name='details'),
	url(r'^details1/$',details1,name='details1'),
	url(r'^hostel/$',hostelPortal,name='hostel'),
	url(r'^hostelChange/$',hostelAllot, name='Hostel Change'),
	url(r'createID/$',createIdCard,name = 'createID'),
	url(r'submitID/$',submitId,name = 'submitID'),
	url(r'^idCard/$',IdCard, name='idCard'),
]