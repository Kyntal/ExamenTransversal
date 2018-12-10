from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.administrador, name='home'),
	url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
]
