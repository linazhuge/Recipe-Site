import cgi
import http
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import InputForm, EditForm
from .models import Recipe
from django.views.generic import ListView
import requests
from django.views import generic
from bs4 import BeautifulSoup
from .functions import check_details, choose_colour
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def selectr_view(request):
    context = {
        'username': 'hello',
    }
    form = InputForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save(commit=False)
        form.save(commit=False).user = request.user
        form.save()
        messages.success(request, "Recipe Submitted!")
        form = InputForm()
        
    
    context['form'] = form

    return render(request, 'input.html', context)


#shows all the recipes in a table for the specific user
@login_required
def showall_view(request):
    context = {
        'recipes': Recipe.objects.filter(user = request.user).order_by('title')
    }
    return render(request, 'showall.html', context)

# shows the recipe in a simplified format
def recipe_view(request, pk):
    current_recipe = Recipe.objects.get(pk=pk)
    check_details(current_recipe)
    if(current_recipe.colour == '#FF0000'):
        colour = choose_colour(current_recipe)
        current_recipe.colour = colour
        current_recipe.save()
    else:
        colour = current_recipe.colour
    
    r = requests.get(current_recipe.recipe)
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_="loc article-post-header")
    desc = s.find('p', class_="comp type--dog article-subheading")

    context = {
        'recipe_name': current_recipe.title,
        'recipe_link': current_recipe.recipe,
        'description': desc.getText(),
        'ingredients': current_recipe.ingres,
        'instructions': current_recipe.instruct, 
        'image': current_recipe.image,
        'colour': colour
    }
    return render(request, 'recipe.html', context)

# shows the editing page of the object pk
def edit_view(request, pk):
    current_recipe = Recipe.objects.get(pk=pk)
    check_details(current_recipe)
    
    ingres = ' '
    ingres = ingres.join(current_recipe.ingres)
    instruct = ' '
    instruct = instruct.join(current_recipe.instruct)
    context = {
        'recipe_name': current_recipe.title,
        'ingredients': ingres,
        'instructions': instruct,
    }
    json = current_recipe.ingres

    form = EditForm(request.POST or None, instance=current_recipe)

    if request.method=="POST":
        if form.is_valid():
            form.save()
    else:
        print("1here")
        current_recipe.title = request.GET.get('title')
        current_recipe.ingres = request.GET.get('ingres')
        current_recipe.instruct = request.GET.get('instruct')

    context['form'] = form

    return render(request, 'edit.html', context)

def delete_view(request, pk):
    current_recipe = Recipe.objects.get(pk=pk)
    
    if request.method == 'POST':
        current_recipe.delete()
        return redirect('showall')
    
    context = {
        'name': current_recipe.title
    }
    return render(request, 'delete.html', context)