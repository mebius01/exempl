from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from blog.models import Post


def index(request):
	post_title = Post.objects.all().get(id=1).title
	post_time = Post.objects.all().get(id=1).created
	post_body = Post.objects.all().get(id=1).body
	post_slug = Post.objects.all().get(id=1).slug

	return render(request, 'blog/post' , {'post_title': post_title, 'post_time': post_time, 'post_body': post_body, 'post_slug': post_slug})

def generic(request):
	post_title = Post.objects.all().get(id=1).title
	post_time = Post.objects.all().get(id=1).created
	post_body = Post.objects.all().get(id=1).body
	return render(request, 'blog/generic.html',  {'post_title': post_title, 'post_time': post_time, 'post_body': post_body})

def elements(request):
	return render(request, 'blog/elements.html')

def list_post(request):
	post_title = Post.objects.all().get(id=1).title
	post_time = Post.objects.all().get(id=1).created
	post_body = Post.objects.all().get(id=1).body
	post_slug = Post.objects.all().get(id=1).slug
	return render(request, 'blog/list_post', {'post_title': post_title, 'post_time': post_time, 'post_body': post_body, 'post_slug': post_slug})


def main(request):
	temp_post = "TEMP POST"
	return render(request, 'main.html' ,{'title':"title of the page", 'temp_post': temp_post})
