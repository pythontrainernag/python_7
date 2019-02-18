from django.http import HttpResponse, JsonResponse

def first(request):
    return HttpResponse("This is my first View")

def first_header(request):
    return HttpResponse("<h1>This is my first View</h1>")

def first_json(request):
    d = {'first': 'First view', 'firh': 'first header view'}
    return JsonResponse(d)