from platform import version
from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="انواع دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مقاله")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name='پوزیشن')

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['position']
    def __str__(self):
        return self.title

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    title = models.CharField(max_length=200, verbose_name="عنوان")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مقاله")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی")
    description = models.TextField(verbose_name="توضیحات")
    thumbnail = models.ImageField(upload_to='images',  verbose_name="تصویر")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات" 
    def __str__(self):
        return self.title
class User():
    pass

class Admin():
    pass

# class User(models.Model):
#     user_id = models.CharField(max_length=200), 
#     username = models.CharField(max_length=200), 
#     language = models.CharField(max_length=200), 
#     number_of_files_sent = models.CharField(max_length=200)

# class Admin(models.Model):
#     admin_user_id = models.CharField(max_length=200), 
#     is_owner = models.CharField(max_length=200)