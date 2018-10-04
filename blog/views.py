from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from blog.models import Post, Comments
from blog.forms import PostForm, UserLoginForm, CommentForm
from pytils.translit import slugify
# from django.contrib import auth
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages


# post = Post.objects.all()
cloud = Post.tags.most_common()


def test(request):
	post = Post.objects.all().last()
	return render(request, 'blog/test' , {'cloud': cloud,  'post': post})


def sing_up(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth.login(request, user)
			return render(request, 'blog/news_blog')
	else:
		form = UserCreationForm()
	return render(request, 'blog/sing_up', {'form': form})

	# if request.method == 'POST':
	# 	form = PostForm(request.POST, request.FILES)
	# 	slug_save = form.save()
	# 	slug_save.slug = slugify(slug_save.title)
	# 	if form.is_valid():
	# 		form.save()
	# 		# return HttpResponseRedirect(reverse('read_post', {'slug': slug}))
	# 		return render(request, 'blog/new_post', {'cloud': cloud, 'complite': "complite"})
	# else:
	# 	form = PostForm()
	# return render(request, 'blog/new_post', {'cloud': cloud, 'form': form})

def index(request):
	post = Post.objects.all().last()
	return render(request, 'blog/index' , {'cloud': cloud,  'post': post})


def list_post(request, tag_slug=None):
	post_list_all = Post.objects.all().order_by('-publish')
	tag = None
	if tag_slug:
		tag = get_object_or_404(Tag, slug=tag_slug)
		post_list_all = post_list_all.filter(tags__in=[tag])

	paginator = Paginator(post_list_all, 4)
	page = request.GET.get('page')
	try:
		page_list = paginator.page(page)
	except PageNotAnInteger:
        # Если страница не является целым числом, показать первую страницу.
		page_list = paginator.page(1)
	except EmptyPage:
        # Если страница выходит за пределы допустимого диапазона (например, 9999), казать последнюю страницу результатов
		page_list = paginator.page(paginator.num_pages)
	return render(request, 'blog/list_post', {'cloud': cloud,  'page': page, 'page_list': page_list,'tag': tag})


def about_blog(request):
	return render(request, 'blog/about_blog', {'cloud': cloud, })



def new_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		slug_save = form.save()
		slug_save.slug = slugify(slug_save.title)
		if form.is_valid():
			form.save()
			# return HttpResponseRedirect(reverse('read_post', {'slug': slug}))
			return render(request, 'blog/new_post', {'cloud': cloud, 'complite': "complite"})
	else:
		form = PostForm()
	return render(request, 'blog/new_post', {'cloud': cloud, 'form': form})

	
def log_in(request):
	if request.user.is_authenticated:
		return render(request, 'blog/news_blog')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
		else:
			messages.error(request, 'Error wrong username/password')
	return render(request, 'blog/log_in')
	# form = UserLoginForm(request.POST or None)
	# context = { 'form': form, }
	# return render(request, 'blog/log_in', {'cloud': cloud,  'form': form, })


def news_blog(request):
	# cloud = Tag.objects.all().annotate(c=Count('post')).filter(c__gt=0)
	return render(request, 'blog/news_blog', {'cloud': cloud, })# {'cloud': cloud})



def read_post(request, slug):
	post = Post.objects.get(slug=slug)
	tag = post.tags.all()
	comment_all = Comments.objects.filter(post_id=post)
	return render(request, 'blog/read_post', {'cloud': cloud, 'tag': tag, 'post': post, 'comment_all': comment_all})

