from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from blog.models import Post


def index(request):

	post_title = Post.objects.all().last().title
	post_time = Post.objects.all().last().created
	post_body = Post.objects.all().last().body
	post_slug = Post.objects.all().last().slug
	return render(request, 'blog/post' , {'post_title': post_title, 'post_time': post_time, 'post_body': post_body, 'post_slug': post_slug})

def list_post(request):
	post_all=[]
	for i in Post.objects.all().order_by('-publish'):
		post_all.append([i.title, i.created, i.body, i.slug ])
	return render(request, 'blog/list_post', {'post_all': post_all})

def read_post(request, slug):
	post_title = Post.objects.filter(slug=slug).get().title
	post_time = Post.objects.filter(slug=slug).get().created
	post_body = Post.objects.filter(slug=slug).get().body
	post_slug = Post.objects.filter(slug=slug).get().slug
	return render(request, 'blog/read_post', {'post_title': post_title, 'post_time': post_time, 'post_body': post_body, 'post_slug': post_slug})
