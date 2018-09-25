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
	TAGS_CHOICES = (
		('Linux','linux'),
		('Django','django'),
		('Python','python'),
		)
	title = models.CharField(max_length=250)

	slug = models.SlugField(max_length=250, unique_for_date='publish', verbose_name='URL',)# default=slugify('0'))
	# author = models.ForeignKey(User, related_name='blog_posts')
	body = RichTextUploadingField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
	tag_choice = models.CharField(max_length=250, choices=TAGS_CHOICES)
	tags = TaggableManager()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return (self.slug)


