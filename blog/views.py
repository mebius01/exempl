from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from blog.models import Post
from blog.forms import PostForm, UserLoginForm

from django.contrib import auth
from django.shortcuts import redirect



def index(request):
	post_title = Post.objects.all().last().title
	post_time = Post.objects.all().last().created
	post_body = Post.objects.all().last().body
	post_slug = Post.objects.all().last().slug
	return render(request, 'blog/index' , \
		{'post_title': post_title, 'post_time': post_time, 'post_body': post_body, 'post_slug': post_slug})

def list_post(request):
	post_all=[]
	for i in Post.objects.all().order_by('-publish'):
		post_all.append([i.title, i.created, i.body, i.slug ])
	return render(request, 'blog/list_post', {'post_all': post_all})

def about_blog(request):
	return render(request, 'blog/about_blog')

def new_post(request):
	form = PostForm(request.POST)
	if form.is_valid():
		form_save = form.save()
		
	else:
		form = PostForm()
		return render(request, 'blog/new_post', {'form': form,})

def new_post_complite(request):
	return render(request, 'blog/new_post_complite')
	
def log_in(request):
	form = UserLoginForm(request.POST or None)
	context = { 'form': form, }
	# if request.method == 'POST' and form.is_valid():
	# 	username = form.cleaned_data.get('username', None)
	# 	password = form.cleaned_data.get('password', None)
	# 	user = auth.authenticate(username=username, password=password)
	# 	if user and user.is_active:
	# 		auth.login(request, user)
	# 		return redirect('blog/index')
	# Основные методы обработки форм https://djbook.ru/examples/19/
	# Глава 5 "Формы" из книги Pro Django https://djbook.ru/examples/57/
	# Список всех рецептов https://djbook.ru/forum/topic/5331/
	return render(request, 'blog/log_in', context)



def news_blog(request):
	return render(request, 'blog/news_blog')



def read_post(request, slug):
	post = Post.objects.get(slug=slug)
	return render(request, 'blog/read_post', \
		{'post_title': post.title, 'post_time': post.created, 'post_body': post.body, 'post_slug': post.slug})

