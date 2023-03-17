from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# its like a table


class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=160)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=60)
    servings = models.IntegerField()
    servings_time_unit = models.CharField(max_length=60)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
