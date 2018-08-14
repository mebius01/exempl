from django.shortcuts import render
from django.http import HttpResponse

def indexpage(request):
	return render(request, 'mainpage/index.html')

def contact(request):
	header = "Personal Data"                    
	langs = ["English", "German", "Spanish"]
	user ={"name" : "Tom", "age" : 23} 
	addr = ("Абрикосовая", 23, 45)
	data = {"header": header, "langs": langs, "user": user, "address": addr}

	return render(request, 'mainpage/contact.html', context=data)

def product(request, productid):
	output = "<h3>Product № {0}</h3>".format(productid)
	return HttpResponse(output)

def users(request, id, name):
	output = "<h2User</h2><h3>id: {0} name: {1}</h3>".format(id, name)
	return HttpResponse(output)

def menu(request):
	return render(request, 'mainpage/menu.html')