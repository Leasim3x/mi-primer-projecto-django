from django.http import HttpResponse, JsonResponse
from .models import Project, Task # "." indica que la carpeta se encuentra en la misma ruta que este archivo
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    return HttpResponse("Index page")

def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)

def about(request):
    return HttpResponse('About')

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def task(request, title):
    task = Task.objects.get(title = title)
    #task = get_object_or_404(Task, id = id)
    return HttpResponse('task: %s' % task.title)