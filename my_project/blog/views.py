from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404

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

def detail(request, slug):
    # try:
    #     article = Article.objects.get(slug=slug)
    # except Exception as e:
    #     raise Http404
    # context = {
    #     # "articles": Article.objects.all() 
    #     "articles": Article.objects.get(slug=slug) 
    # }
    context = {
        # "articles": Article.objects.all() 
        "articles": get_object_or_404(Article, slug=slug, status="p") 
    }
    return render(request, "blog/detail.html", context)