from django.urls import path
from . views import project, projects

urlpatterns = [
    path('', projects, name='projects'),
    path('project/<str:pk>/', project, name='project')
]
