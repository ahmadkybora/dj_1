from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Article

# Create your views here.
def home(request):
    # context = {
    #     "articles": [
    #         {
    #             "id": 1,
    #             "title": "ss", 
    #             "desc": "ss",
    #             "img": "s"
    #         },
    #         {
    #             "id": 2,
    #             "title": "ss", 
    #             "desc": "ss",
    #             "img": "s"
    #         },
    #         {
    #             "id": 3,
    #             "title": "ss", 
    #             "desc": "ss",
    #             "img": "s"
    #         },
    #         {
    #             "id": 4,
    #             "title": "ss", 
    #             "desc": "ss",
    #             "img": "s"
    #         }
    #     ]
    # }
    context = {
        # "articles": Article.objects.all() 
        "articles": Article.objects.filter(status="p").order_by("-publish")[:3] 
    }
    return render(request, "blog/home.html", context)

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