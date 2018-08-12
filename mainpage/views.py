from django.shortcuts import render
from jinja2 import Template
from django.http import HttpResponse

def indexpage(request):
	return render(request, 'mainpage/index.html')

def contact(request):
	data = {'header': "Hello", 'message': 'Welcome to the page Contact'}
	return render(request, 'mainpage/contact.html', context=data)

def product(request, productid):
	output = "<h3>Product № {0}</h3>".format(productid)
	return HttpResponse(output)

def users(request, id, name):
	output = "<h2User</h2><h3>id: {0} name: {1}</h3>".format(id, name)
	return HttpResponse(output)
