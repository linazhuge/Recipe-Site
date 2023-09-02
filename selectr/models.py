from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField
from django.core.exceptions import ValidationError


# Create your models here.

def validate_allrecipes(value):
    if "allrecipes" not in value:
        raise ValidationError(
            ("!This recipe is not from allrecipes."),
            params={"value": value},
        )

class Recipe(models.Model):
    title = models.CharField(max_length=30)
    recipe = models.URLField(validators=[validate_allrecipes], max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    ingres = models.JSONField(default=dict)
    instruct = models.JSONField(default=dict)
    image = models.URLField(max_length=500)
    colour = ColorField(default='#FF0000')

    def __str__(self):
        return self.title


