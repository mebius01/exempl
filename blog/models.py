from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
 

class Post(models.Model):

	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
	# TAGS_CHOICES = (
	# 	('Linux','linux'),
	# 	('Django','django'),
	# 	('Python','python'),
	# 	)
	title = models.CharField(max_length=250)

	slug = models.SlugField(max_length=250, unique_for_date='publish', verbose_name='URL',)# default=slugify('0'))
	# author = models.ForeignKey(User, related_name='blog_posts')
	body = RichTextUploadingField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
	# tag_choice = models.CharField(max_length=250, choices=TAGS_CHOICES)
	tags = TaggableManager(help_text = "Список тегов, разделенных запятыми.", through=None)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return (self.slug)


class Comments(models.Model):
	post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ('created',)
	def __str__(self):
		return 'Comment by {} on {}'.format(self.name, self.post)