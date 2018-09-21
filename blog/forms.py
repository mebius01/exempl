
from django import forms
from django.utils.translation import ugettext as _
from django.forms import ModelForm
from blog.models import Post


class PostForm(ModelForm):

	class Meta:
		model = Post
		fields = ['title', 'body']

# class PostModelForm(Mo)

# class PostForm(forms.Form):

# 	title = forms.CharField(max_length=250)
# 	body = forms.CharField(required=False, widget=forms.Textarea)
# 	class Meta:
# 		model = Post
# 		fields = ('title', 'body',)

# https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Forms
# https://translate.google.com/translate?sl=en&tl=ru&js=y&prev=_t&hl=ru&ie=UTF-8&u=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F2.1%2Ftopics%2Fforms%2Fmodelforms%2F&edit-text=
# https://pocoz.gitbooks.io/django-v-primerah/content/glava-2-uluchshenie-bloga-s-pomoshyu-rasshirennyh-vozmozhnostej/sozdanie-sistemy-kommentariev/obrabotka-modelforms-v-predstavleniyah.html
# https://stackoverflow.com/questions/22739701/django-save-modelform
# https://www.simplifiedpython.net/django-modelform-example/


# https://djbook.ru/rel1.9/topics/forms/modelforms.html Передача начальных значений
# https://code-examples.net/ru/docs/django~2.0/index

class UserLoginForm(forms.Form):
	username = forms.CharField(label=_(u'Username'), max_length=30)
	password = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput)