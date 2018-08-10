from django.shortcuts import render

from django.http import HttpResponse

def indexpage(request):
	return render(request, 'mainpage/index.html', {})