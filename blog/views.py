from django.shortcuts import render, get_object_or_404
# from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from blog.models import Post
from blog.forms import PostForm, UserLoginForm
from pytils.translit import slugify
# from django.contrib import auth
from taggit.models import Tag


def index(request):
	post = Post.objects.all().last()
	return render(request, 'blog/index' , \
		{'post_title': post.title, 'post_time': post.created, 'post_body': post.body, 'post_slug': post.slug})

def list_post(request, tag_slug=None):
	object_list = Post.objects.all().order_by('-publish')
	tag = None
	post_all=[]
	if tag_slug:
		tag = get_object_or_404(Tag, slug=tag_slug)
		object_list = object_list.filter(tags__in=[tag])
	for i in object_list:
		post_all.append([i.title, i.created, i.body, i.slug ])
	return render(request, 'blog/list_post', {'post_all': post_all, 'tag': tag})

def about_blog(request):
	return render(request, 'blog/about_blog')


# if request.method == "POST" :
#     form = MyFormClass ( request . POST )
#     if form.is_valid ():
#         obj = form.save( commit = False )
#         obj.user = request.user
#         obj.save()
#         # Without this next line the tags won't be saved.
#         form . save_m2m ()
# https://translate.google.com/translate?sl=en&tl=ru&js=y&prev=_t&hl=ru&ie=UTF-8&u=https%3A%2F%2Fdjango-taggit.readthedocs.io%2Fen%2Flatest%2Fforms.html&edit-text=
def new_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		slug_save = form.save()
		slug_save.slug = slugify(slug_save.title)
		if form.is_valid():
			form.save()
			# return HttpResponseRedirect(reverse('read_post', {'slug': slug}))
			return render(request, 'blog/new_post', {'complite': "complite"})
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
	tag = Post.tags.all()
	return render(request, 'blog/read_post', \
		{'tag': tag, 'post': post}) #'post_title': post.title, 'post_time': post.created, 'post_body': post.body, 'post_slug': post.slug})

# Установка и настройка CKEditor для проекта на Django 1.9.
# https://tiv.space/?page=4
# !!!!!!
# Django - CKEditor Tutorial With CodeSnippet Syntax Highlighting
# https://www.wdtutorials.com/django/ckeditor-tutorial-codesnippet-syntax-highlighting/
# !!!!!!
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

# django_taggit

# https://godjango.com/33-tagging-with-django-taggit/
# http://www.autister.com/post/62-uroki-django-kak-dobavit-k-state-tegi-i-sdelat-filtr-po-tegam/
# Привязка tag_id, object_id, m2m.
# https://ru.stackoverflow.com/questions/496764/django-%d0%9a%d0%b0%d0%ba-%d0%b2%d1%8b%d0%b2%d0%b5%d1%81%d1%82%d0%b8-%d1%82%d1%8d%d0%b3%d0%b8-%d0%b2-%d1%88%d0%b0%d0%b1%d0%bb%d0%be%d0%bd%d0%b5
# https://djbook.ru/forum/topic/5789/
# https://codefellows.github.io/sea-python-401d5/lectures/django_taggit.html


# Пагинатор
# https://docs.djangoproject.com/en/2.1/topics/pagination/