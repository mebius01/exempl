from blog.models import Post
from django import template
from taggit.models import Tag
register = template.Library()

@register.simple_tag
def tags_list():
	cloud = Post.tags.most_common()
	return cloud
