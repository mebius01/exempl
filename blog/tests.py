from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from blog.views import *

class SignUpTests(TestCase):
	def test_signup_status_code(self):
		url = reverse('sign_up/')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)

	def test_signup_url_resolves_signup_view(self):
		view = resolve('sign_up/')
		self.assertEquals(view.func, signup)
