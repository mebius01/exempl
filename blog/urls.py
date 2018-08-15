from django.urls import path, include, re_path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('index.html', views.index, name='index'),
	path('generic.html', views.generic, name='generic'),
	path('elements.html', views.elements, name='elements'),

]