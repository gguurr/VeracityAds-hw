from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.CharField(max_length=50)