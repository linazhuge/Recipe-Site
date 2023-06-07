from django import forms
from .models import Recipe


class InputForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'recipe']