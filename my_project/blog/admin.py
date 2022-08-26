from re import search
from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'status')
    list_fiter = ('publish', 'status')
    search_filter = ('title', 'description')
    prepopulated_fields = {'slug': ('title')}
admin.site.register(Article)