import json
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Recipe

class InputForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'recipe']

class EditForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingres', 'instruct']
        labels = {
            'title': "Name",
            'ingres': "Ingredients",
            'instruct': "Instructions"
        }
        
        
        

        