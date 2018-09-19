from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from blog.models import Post


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
	text = 'THIS IS TEST'
	return render(request, 'blog/new_post', {'text': text})


def read_post(request, slug):
	post_title = Post.objects.get(slug=slug).title
	post_time = Post.objects.get(slug=slug).created
	post_body = Post.objects.get(slug=slug).body
	post_slug = Post.objects.get(slug=slug).slug
<<<<<<< HEAD
	return render(request, 'blog/read_post', {'post_title': post_title, 'post_time': post_time, 'post_body': post_body, 'post_slug': post_slug})
=======
	return render(request, 'blog/read_post', \
		{'post_title': post_title, 'post_time': post_time, 'post_body': post_body, 'post_slug': post_slug})

# 'WTF with new_post about_blog'
>>>>>>> 0cd44c77e7c609c83970edab23a9f90bf5ff9489
