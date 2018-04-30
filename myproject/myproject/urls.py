"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout, login
from django.views.static import serve

urlpatterns = [
    url(r'estatico/(.*)$', serve, {'document_root': 'templates/Summer_Breeze'}),
    url(r'^accounts/profile/$', 'cms_post.views.annotated_barra'), #apaño para cuando haces login desde la barra
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout', logout),
    url(r'^login', login),
    url(r'^annotated/$', 'cms_post.views.annotated_barra'),
    url(r'^$', 'cms_post.views.barra'),
    url(r'^annotated/content/(\d+)$', 'cms_post.views.annotated_content'),
    url(r'^content/(\d+)$', 'cms_post.views.content'),
    url(r'^edit/content/(\d+)$', 'cms_post.views.edit_content'),
    url(r'^edit/annotated/content/(\d+)$', 'cms_post.views.edit_annotated_content'),


]
