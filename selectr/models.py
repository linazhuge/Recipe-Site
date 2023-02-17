from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    recipe = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    ingres = models.JSONField(default=" ")
    instruct = models.JSONField(default=" ")
    image = models.URLField()

    def __str__(self):
        return self.title

