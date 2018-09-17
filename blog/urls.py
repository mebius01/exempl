from django.urls import path, include, re_path
from blog import views

urlpatterns = [
	# path('', views.index),
	# path('create/', views.create),
	path('', views.index, name='index'),
	path('index', views.index, name='index'),
	path('list_post', views.list_post),
	path('<slug>', views.read_post),



]