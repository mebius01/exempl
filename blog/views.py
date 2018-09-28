from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from blog.models import Post, Comments
from blog.forms import PostForm, UserLoginForm, CommentForm
from pytils.translit import slugify
# from django.contrib import auth
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
	post = Post.objects.all().last()
	return render(request, 'blog/index' , {'post': post})


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
	return render(request, 'blog/list_post', {'page': page, 'page_list': page_list,'tag': tag})


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
	tag = post.tags.all()
	comment_form = CommentForm(request.POST, request.FILES)
	
	if comment_form.is_valid():
		comment_form.save()
		return render(request, 'blog/read_post', {'complite': "complite"})
	else:
		comment_form = CommentForm()
	return render(request, 'blog/read_post', {'tag': tag, 'post': post, 'comment_form': comment_form})

