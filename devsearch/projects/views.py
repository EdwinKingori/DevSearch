from django.shortcuts import render, redirect
from .models import Project, Reviews, Tag
from .forms import ProjectForm
# Create your views here.


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


def createProject(request):
    form = ProjectForm()
  # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
        # redirect user after filling the form
        return redirect('projects')
    context = {'form': form}
    return render(request, "projects/project_form.html", context)
