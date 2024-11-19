from django.http import JsonResponse


def getRoutes(request):

    routes = [
        {'GET': 'api/projects'},
        {'GET': 'api/projects/id'},
        {'POST': 'api/projects/id/vote'},

        {'POST': 'api/users/token'},
        # use refresh to keep the user signed in the page
        {'GET': 'api/users/token/refresh'},

    ]

    # safe reurns more than a python dictionary
    return JsonResponse(routes, safe=False)
