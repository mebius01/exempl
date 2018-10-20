
from django import forms
from django.utils.translation import ugettext as _
from django.forms import ModelForm
from blog.models import Post, Comments
#from ckeditor_uploader.fields import RichTextUploadingField
from pagedown.widgets import PagedownWidget


class PostForm(ModelForm):
	# body = forms.CharField(widget=PagedownWidget())
	title = forms.CharField(max_length=250, label='',)

	class Meta:
		model = Post
		fields = ['body', 'tags', 'title']

class UserLoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
	
	class Meta:
		model = ModelForm
		fields = ['username','password']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ['name', 'email', 'body']
