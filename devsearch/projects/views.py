from django.shortcuts import render, redirect
from .models import Project, Reviews, Tag
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html',
                  context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single_project.html',
                  {'project': projectObj,
                   'tags': tags})

# Creating/posting data in the modeldatabase


@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()
  # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form.save()
        # redirect user after filling the form
        return redirect('projects')
    context = {'form': form}
    return render(request, "projects/project_form.html", context)

# Updating data in the modeldatabase


@login_required(login_url='login')
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

  # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST, request.FILES, instance=project)
        # check whether it's valid:
        if form.is_valid():
            form.save()
        # redirect user after filling the form
        return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url='login')
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == "POST":
        project.delete()
        return redirect("projects")
    context = {'object': project}
    return render(request, 'projects/delete.html', context)
