from django.http import HttpResponse
from .models import Project, Task # "." indica que la carpeta se encuentra en la misma ruta que este archivo
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateNewProject

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
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

"""def task(request, title):
    task = Task.objects.get(title = title)"""
def tasks(request):
    #task = get_object_or_404(Task, id = id)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description = request.POST['description'], project_id=2)
        return redirect('tasks/')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {'form': CreateNewProject()
                                                                })
    else:
        print(request.POST)
        project = Project.objects.create(name=request.POST["name"])
        print(project)
        return render(request, 'projects/create_project.html', {'form': CreateNewProject()
                                                                })