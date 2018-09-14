"""exempl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
# from mainpage import views
# from blog import views

# mainpage_patterns = [
# 	path('', views.indexpage, name='indexpage'),
#     re_path(r'^contact/', views.contact, name='Контакты'),
#     path('product/<int:productid>/', views.product),
#     path('users/<int:id>/<str:name>/', views.users),
#     path('menu/', views.menu, name='menu'),
# ]

# blog_patterns = [
# 	path('', views.index, name='index'),

# ]

 

urlpatterns = [
	path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),

]

