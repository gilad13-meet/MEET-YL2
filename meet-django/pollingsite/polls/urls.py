from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
	# ex. /polls/index
	url(r'^index/$', views.index , name="index")
)
