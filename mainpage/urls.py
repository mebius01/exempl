from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.indexpage, name='indexpage'),
    re_path(r'^contact/', views.contact, name='Контакты'),
    path('product/<int:productid>/', views.product),
    path('users/<int:id>/<str:name>/', views.users),
    path('menu/', views.menu, name='menu'),
]