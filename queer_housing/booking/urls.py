from django.conf.urls import patterns, url

from booking import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<User_id>\d+)/$', views.UserView, name='user'),
#	url(r'^(?P<pk>\d+)/houses$', views.HousesView.as_view(), name='houses'),
)