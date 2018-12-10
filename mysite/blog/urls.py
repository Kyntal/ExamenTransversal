from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.views import logout
from . import views
from .views import nuevoproducto
from .views import registroventa
from .views import vendedor

urlpatterns = [
	url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
	url(r'social-auth/', include('social_django.urls', namespace='social')),
	url(r'^$', views.administrador, name='inicio'),
	url(r'^nuevatienda/$', views.nuevatienda, name = 'nuevatienda'),
	url(r'^nuevo-producto/$', nuevoproducto, name = 'nuevoproducto'),
	url(r'^registro-venta/$', registroventa, name = 'registroventa'),
	url(r'^vendedor/$', vendedor, name = 'vendedor'),
]
