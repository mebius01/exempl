from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'publish', 'status', 'get_absolute_url',)
	prepopulated_fields = {'slug': ('title',)}
	

admin.site.register(Post, PostAdmin)