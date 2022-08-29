from django.db import models
from django.utils import timezone

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

class User(models.Model):
    user_id = models.CharField(max_length=200), 
    username = models.CharField(max_length=200), 
    language = models.CharField(max_length=200), 
    number_of_files_sent = models.CharField(max_length=200)

class Admin(models.Model):
    admin_user_id = models.CharField(max_length=200), 
    is_owner = models.CharField(max_length=200)