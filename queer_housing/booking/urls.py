from django.conf.urls import patterns, url

from booking import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
#	url(r'^(?P<pk>\d+)/users$', views.UsersView.as_view(), name='users'),
#	url(r'^(?P<pk>\d+)/houses$', views.HousesView.as_view(), name='houses'),
)