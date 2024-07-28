from django.urls import path
from . views import project, projects

urlpatterns = [
    path('', project, name='project'),
    path('projects/', projects, name='projects')
]
