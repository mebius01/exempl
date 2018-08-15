from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'blog/index.html')

def generic(request):
	return render(request, 'blog/generic.html')

def elements(request):
	return render(request, 'blog/elements.html')
	pass