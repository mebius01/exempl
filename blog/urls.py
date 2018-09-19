from django.urls import path, include, re_path
from blog import views

urlpatterns = [
	path('', views.index, name='index'),
	path('index/', views.index, name='index'),
	path('list_post/', views.list_post, name='list_post'),
	path('about_blog/', views.about_blog, name='about_blog'),
	path('new_post/', views.new_post, name='new_post'),
	path('<slug>/', views.read_post, name='read_post'),
]
# http://softwaremaniacs.org/blog/2006/08/04/url-reverse/ URL в шаблонах через reverse
# http://www.autister.com/post/44-kak-sdelat-v-django-chpu-url-ili-chto-takoe-slug/ Как сделать в Django ЧПУ url или что такое Slug 
# https://djbook.ru/rel1.8/ref/models/instances.html#get-absolute-url 
# http://qaru.site/questions/1948421/generating-unique-slug-in-django Создание уникальной пули в Django
# http://sudnitsina.pythonanywhere.com/