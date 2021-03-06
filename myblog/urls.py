"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

import blogapp.views as bv


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include(('blogapp.urls', 'blogapp'), namespace='blog')),
    url(r'^$', bv.homepage),
    url(r'^login/$', bv.login, name='login'),
    url(r'^register/$', bv.register, name='register'),
    url(r'logout/$', bv.logout, name='logout'),
    url(r'^download/(?P<file>.*)', bv.download, name='download'),
    url(r'^chatroom/$', bv.chatroom, name='chatroom')
]
