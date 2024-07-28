from django.shortcuts import render

# Create your views here.


def project(request):
    return render(request, 'projects/index.html')


def projects(request):
    return render(request, 'projects/projects.html')
