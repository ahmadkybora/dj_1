from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return HttpResponse('hello')

def api(request):
    data = {
        "1": {
            "id": 1,
            "title": "hello"
        },
        "2": {
            "id": 1,
            "title": "hello"
        },
        "3": {
            "id": 1,
            "title": "hello"
        },
    }
    return JsonResponse(data)