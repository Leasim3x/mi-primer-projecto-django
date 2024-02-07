from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<int:id>', views.hello),
    path('projects/', views.projects),
    #path('task/<str:title>', views.task),
    path('tasks/', views.tasks),
    path('create_task', views.create_task),
    path('create_project', views.create_project),
]