from django.shortcuts import render, get_object_or_404
# from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from blog.models import Post
from blog.forms import PostForm, UserLoginForm
from pytils.translit import slugify
# from django.contrib import auth



def index(request):
	post = Post.objects.all().last()
	return render(request, 'blog/index' , \
		{'post_title': post.title, 'post_time': post.created, 'post_body': post.body, 'post_slug': post.slug})

def list_post(request):
	post_all=[]
	for i in Post.objects.all().order_by('-publish'):
		post_all.append([i.title, i.created, i.body, i.slug ])
	return render(request, 'blog/list_post', {'post_all': post_all})

def about_blog(request):
	return render(request, 'blog/about_blog')

def new_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		slug_save = form.save()
		slug_save.slug = slugify(slug_save.title)
		if form.is_valid():
			form.save()
			# return HttpResponseRedirect(reverse('read_post', {'slug': slug}))
			# return render(request, 'blog/new_post', {'complite': "complite"})
	else:
		form = PostForm()
	return render(request, 'blog/new_post', {'form': form})

	
def log_in(request):
	form = UserLoginForm(request.POST or None)
	context = { 'form': form, }
	return render(request, 'blog/log_in', context)



def news_blog(request):
	return render(request, 'blog/news_blog')



def read_post(request, slug):
	post = Post.objects.get(slug=slug)
	return render(request, 'blog/read_post', \
		{'post_title': post.title, 'post_time': post.created, 'post_body': post.body, 'post_slug': post.slug})

# Предварительный просмотр форм
# https://djbook.ru/rel1.9/ref/contrib/formtools/form-preview.html

# Теги в блоге
# https://github.com/alex/django-taggit

# Батарейки для Данго
# https://habr.com/post/136168/

# Поиск:
		# django-haystack
		# http://haystacksearch.org/
		# django-sphinx
		# https://github.com/jorgecarleitao/django-sphinxql