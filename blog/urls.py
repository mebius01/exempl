from django.urls import path, include, re_path
from blog import views

urlpatterns = [
	# path('', views.index),
	# path('create/', views.create),
	path('', views.index, name='index'),
	path('index', views.index, name='index'),
	path('list_post', views.list_post),
	path('<slug:title>', views.generic, name='generic'),
	path('elements.html', views.elements, name='elements'),



]