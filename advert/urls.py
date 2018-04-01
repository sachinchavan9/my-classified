from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_view.login, {'template_name': 'advert/login.html'}, name='login'),
    url(r'^logout/$', auth_view.logout, name='logout'),
    url(r'^(?P<slug>[ \w-]+)/$', views.district_view, name='city_view'),
    url(r'(?P<pk>\d+)/(?P<slug>[ \w-]+)/$', views.add_view, name='add_view'),
    url(r'(?P<title>[*])/(?P<pk>\d+)/$', views.advert, name='advert'),
]
