from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^irshad/$',views.irshadlanding, name='irshadlanding'),
	url(r'^$',views.post_list, name='post_list'),
]
