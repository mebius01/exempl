from django.shortcuts import render
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
	for i in Post.objects.all():
		post_all.append([i.title, i.created, i.body, i.slug ])
	
	return render(request, 'blog/list_post', {'post_all': post_all})