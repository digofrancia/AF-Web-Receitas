from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
  name = models.CharField(max_length=100)
#   description = models.TextField()
  image = models.URLField(max_length=255, blank=True, null=True)

  def __str__(self):
    return self.name


class Recipe(models.Model):
  category = models.ForeignKey(Category, related_name='recipes', on_delete=models.CASCADE, default=None)
  name = models.CharField(max_length=100)
  rate = models.IntegerField(default=3)
  description = models.TextField()

  ingredients = models.TextField()
  preparation = models.TextField()
  time = models.CharField(max_length=50)
  image = models.URLField(max_length=255, blank=True, null=True)
  serve = models.CharField(max_length=50)

  author = models.ForeignKey(User, on_delete=models.CASCADE)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def get_absolute_url(self):
      return reverse("recipes-detail", kwargs={"pk": self.pk})

  def __str__(self):
    return self.name
  

class Comment(models.Model):
  recipe = models.ForeignKey(Recipe, related_name='comments', on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  comment = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'Comentário feito por {self.name} sobre {self.recipe}'