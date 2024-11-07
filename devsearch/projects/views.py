from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Project, Reviews
from .utils import searchProjects, paginateProjects

# Create your views here.


def projects(request):

    projects, search_query = searchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 6)

    context = {
        'projects': projects,
        'search_query': search_query,
        'custom_range': custom_range
    }
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
    profile = request.user.profile
    form = ProjectForm()

  # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
        # redirect user after filling the form
            return redirect('account')
    context = {'form': form}
    return render(request, "projects/project_form.html", context)

# Updating data in the modeldatabase


@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

  # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST, request.FILES, instance=project)
        # check whether it's valid:
        if form.is_valid():
            form.save()
        # redirect user after filling the form
            return redirect('account')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == "POST":
        project.delete()
        return redirect('account')
    context = {'object': project}
    return render(request, 'delete.html', context)
