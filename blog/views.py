from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from blog.models import Person


def index(request):
	return render(request, 'blog/index.html')

def generic(request):
	return render(request, 'blog/generic.html')

def elements(request):
	return render(request, 'blog/elements.html')

# получение данных из бд
def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})
 
# сохранение данных в бд
def create(request):
    if request.method == "POST":
		tom = Person()
		tom.name = request.POST.get("name")
		tom.age = request.POST.get("age")
		tom.save()
    return HttpResponseRedirect("/")