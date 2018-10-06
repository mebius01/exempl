from blog.models import Post
def tags_top(request):
	return {'cloud': Post.tags.most_common()}
