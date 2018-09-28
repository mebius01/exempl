from django.contrib import admin
from .models import Post, Comments

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'publish', 'status', 'get_absolute_url',)
	prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'post', 'created', 'active')
	list_filter = ('active', 'created', 'updated')
	search_fields = ('name', 'email', 'body')


admin.site.register(Post, PostAdmin)

admin.site.register(Comments, CommentAdmin)