from django.http import HttpResponse
from .models import Project, Task # "." indica que la carpeta se encuentra en la misma ruta que este archivo
from django.shortcuts import render

from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    title = 'Django Couse!!'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    username = 'Misael'
    return render(request, 'about.html', {
        'username': username
    })

def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

"""def task(request, title):
    task = Task.objects.get(title = title)"""
def task(request):
    #task = get_object_or_404(Task, id = id)
    return render(request, 'task.html')