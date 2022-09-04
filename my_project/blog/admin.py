from re import search
from django.contrib import admin
from .models import Article, Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'status')
    list_fiter = (['status'])
    search_filter = ('title', 'description')
    prepopulated_fields = {'slug': ('title')}
admin.site.register(Category)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'status')
    list_fiter = ('publish', 'status')
    search_filter = ('title', 'description')
    prepopulated_fields = {'slug': ('title')}
    
    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category.all()])
    category_to_str.short_description = "زمان انتشار"

admin.site.register(Article)