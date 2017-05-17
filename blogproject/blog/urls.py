#coding:utf-8

from django.conf.urls import url
from . import views
#告诉Django，这个urls模块是属于blog应用的
app_name = 'blog'
urlpatterns = [
		#将类转换成函数，只需调用父类中的as_view()方法
		url(r'^index/$',views.index,name ='index'),
		url(r'^article/(?P<pk>[0-9]+)/$',views.detail,name = 'detail'),
		url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
		url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
		url(r'^about/$',views.about,name ='about'),
		url(r'^contact/$',views.contact,name ='contact'),
]
