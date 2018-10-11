
from django import forms
from django.utils.translation import ugettext as _
from django.forms import ModelForm
from blog.models import Post, Comments
#from ckeditor_uploader.fields import RichTextUploadingField



class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'body', 'tags']

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
