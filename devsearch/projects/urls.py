from django.urls import path
from . views import project, projects, createProject, updateProject, deleteProject

urlpatterns = [
    path('', projects, name='projects'),
    path('project/<slug:slug>/', project, name='project'),
    path('create-project/', createProject, name='create-project'),
    path('update/<str:pk>/', updateProject, name='update'),
    path('delete/<str:pk>', deleteProject, name='delete')
]
