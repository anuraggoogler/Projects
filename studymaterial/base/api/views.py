from django.http import JsonResponse


def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/room',
        'GET /api/rooms/:id'
    ]
    return JsonResponse(routes, safe=False)