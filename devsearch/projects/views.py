from django.shortcuts import render

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
    msg = "You are on the project's page"
    context = {'message': msg, "projects": projectsList}
    return render(request, 'projects/index.html',
                  context)


def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/projects.html',
                  {'project': projectObj})
