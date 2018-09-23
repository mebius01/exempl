
from django import forms
from django.utils.translation import ugettext as _
from django.forms import ModelForm
from blog.models import Post
#from ckeditor_uploader.fields import RichTextUploadingField

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'body']

class UserLoginForm(forms.Form):
	username = forms.CharField(label=_(u'Username'), max_length=30)
	password = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput)