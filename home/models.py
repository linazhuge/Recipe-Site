from django.db import models
from selectr.models import validate_allrecipes

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=30)
    recipe = models.URLField(validators=[validate_allrecipes], max_length=500)
    ingres = models.JSONField(default=dict)
    instruct = models.JSONField(default=dict)
    image = models.URLField(max_length=500)

    def __str__(self):
        return self.title
