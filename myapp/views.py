from django.http import HttpResponse
from .models import Project, Task # "." indica que la carpeta se encuentra en la misma ruta que este archivo
from django.shortcuts import render, redirect, get_object_or_404
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
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def create_task(request):
    print("Entrnado a la vista create_task")
    if request.method == 'GET':
        print("Solicitud GET recibida")
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    elif request.method == 'POST':
        print("Solicitud POST recibida")
        Task.objects.create(title=request.POST["title"], description=request.POST["description"], project_id=2)
        #Task.objects.create(description=request.POST["description"])
        return redirect('tasks')
    else: 
        print("Solicitud HTTP no admitida")
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', 
        {'form': CreateNewProject()})
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect('projects')
    
def project_detail(request, id):
    project = get_object_or_404(Project, id = id)
    tasks = Task.objects.filter(project_id = id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })