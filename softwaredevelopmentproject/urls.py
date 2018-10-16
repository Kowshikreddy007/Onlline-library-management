from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [
    path('adminkowshik/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^student/', include('student.urls')),
]
