from django.urls import path
from .views import home, api, detail

app_name = "blog"
urlpatterns = [
    path('', home, name="home"),
    path('article/<slug:slug>', detail, name="detail"),
    path('api/', api, name="api")
]

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)