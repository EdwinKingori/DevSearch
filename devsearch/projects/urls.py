from django.urls import path
from . views import project, projects, createProject

urlpatterns = [
    path('', projects, name='projects'),
    path('project/<str:pk>/', project, name='project'),
    path('create-project/', createProject, name='create-project')
]
