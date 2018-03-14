from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<slug>[\w-]+)/$', views.district_view, name='city_view'),
    url(r'(?P<pk>\d+)/(?P<slug>[\w-]+)/$', views.add_view, name='add_view'),
    url(r'(?P<title>[\w-]+)/(?P<pk>\d+)/$', views.advert),
]
