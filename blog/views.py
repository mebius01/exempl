from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from blog.models import Post
from blog.forms import PostForm, UserLoginForm
from django.template.defaultfilters import slugify
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
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render(request, 'blog/new_post', {'complite': "complite"})
			# return render(request, 'blog/new_post', {'form': form, 'complite': "complite"})


# Post.objects.order_by('-publish')[:1].get()
# Примечание

# Поля, которые не определены в форме, не будут учитываться при вызове метода save(). Также, если вы вручную добавите в форму исключенные поля, то они не будут заполняться из экземпляра модели.

# Django будет препятствовать всем попыткам сохранить неполную модель. Таким образом, если модель требует заполнения определённых полей и для них не предоставлено значение по умолчанию, то сохранить форму для такой модели не получится. Для решения этой проблемы вам потребуется создать экземпляр такой модели, передав ему начальные значения для обязательных, но незаполненных полей:

# author = Author(title='Mr')
# form = PartialAuthorForm(request.POST, instance=author)
# form.save()

# В качестве альтернативы, вы можете использовать save(commit=False) и вручную определить все необходимые поля:

# form = PartialAuthorForm(request.POST)
# author = form.save(commit=False)
# author.title = 'Mr'
# author.save()

Обратитесь к разделу section on saving forms для подробностей по использованию save(commit=False).
	else:
		form = PostForm()
	return render(request, 'blog/new_post', {'form': form})

	
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

