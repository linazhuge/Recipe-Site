import cgi
from django.shortcuts import render
from .forms import InputForm, EditForm
from .models import Recipe
from django.views.generic import ListView
import requests
from django.views import generic
from bs4 import BeautifulSoup

# Create your views here.

def selectr_view(request):
    context = {
        'username': 'hello',
    }
    form = InputForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save(commit=False)
        form.save(commit=False).user = request.user
        form.save()
        print("saved!")
    
    context['form'] = form

    return render(request, 'select.html', context)


#shows all the recipes in a table for the specific user
def showall_view(request):
    context = {
        'recipes': Recipe.objects.filter(user = request.user)
    }
    print(Recipe.objects.first().recipe)
    print()
    return render(request, 'showall.html', context)

# shows the recipe in a simplified format
def recipe_view(request, pk):
    current_recipe = Recipe.objects.get(pk=pk)
    check_details(current_recipe)
    
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
        'image': current_recipe.image
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
        'instructions': instruct
    }

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

# function that does the webscraping, checks if its been done
def check_details(recipe):
    r = requests.get(recipe.recipe)
    soup = BeautifulSoup(r.content, 'html.parser')

    #loading the instructions
    ins = soup.find('div', class_="comp recipe__steps-content mntl-sc-page mntl-block")
    instr = ins.find_all('p')
    if(recipe.instruct == " "):
        lst_instr = []
        for i in instr:
            lst_instr.append(i.getText())
        recipe.instruct = lst_instr
        recipe.save()
    
    #loading the ingredients
    if(recipe.ingres == " "):
        i = soup.find('div', class_="comp mntl-lrs-ingredients mntl-block")
        ingres = i.find('ul', class_="mntl-structured-ingredients__list")

        lst_ingre = []
        for ing in ingres:
            if(not ing.getText().isspace()):
                lst_ingre.append(ing.getText())
        recipe.ingres = lst_ingre
        recipe.save()

    try:
        i = soup.find('div', class_="img-placeholder")
        im = i.find('img', class_="loaded primary-img--noscript primary-image__image mntl-primary-image--blurry")
        recipe.image = im['src']
    except:
        try:
            print("here")
            i = soup.find('div', class_="img-placeholder")
            im = i.find('img')
            recipe.image = im['src']     
        except:
            i = soup.find('div')
            im = i.find('img')
            recipe.image = im['src']