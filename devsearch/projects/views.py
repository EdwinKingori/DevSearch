from django.shortcuts import render
from .models import Project, Reviews, Tag
# Create your views here.

projectsList = [
    {
        'id': '1',
        'title': "Ecommerce Website",
        'description': "fully Functional devsearch site"
    },
    {
        'id': '2',
        'title': "Portffolio Website",
        'description': "fully Functional personal portfolio site"
    },
    {
        'id': '3',
        'title': "work Website",
        'description': "fully Functional working site"
    },
]


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/index.html',
                  context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/projects.html',
                  {'project': projectObj,
                   'tags': tags})
