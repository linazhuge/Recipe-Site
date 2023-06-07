from bs4 import BeautifulSoup
from django.shortcuts import redirect, render
import requests
from .forms import InputForm
from .models import Recipe

# Create your views here.
def home_view(request):
    user = request.user
    context = {
        'username': 'hello',
        'user': user,
    }
    form = InputForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save(commit=False)
        form.save()
        form.clean()
        return redirect(home_view_recipe)
    
    context['form'] = form
    return render(request, 'homepage.html', context)

def home_view_recipe(request):
    recipe = Recipe.objects.last()
    r = requests.get(recipe.recipe)
    soup = BeautifulSoup(r.content, 'html.parser')

    #loading the instructions
    if(recipe.instruct == " "):
        ins = soup.find('div', class_="comp recipe__steps-content mntl-sc-page mntl-block")
        for tag in ins.find_all('figcaption'):
            tag.decompose()
        instr = ins.find_all('p')
        lst_instr = []
        for i in instr:
            lst_instr.append(i.getText())
        recipe.instruct = lst_instr
    
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
            i = soup.find('div', class_="figure-media")
            im = i.find('img')
            try:
                recipe.image = im['data-src']     
            except:
                recipe.image = im['src']
        except:
            print("no image")

    
    recipe.save()

    context = {
        'recipe_name': recipe.title,
        'recipe_link': recipe.recipe,
        'ingredients': recipe.ingres,
        'instructions': recipe.instruct, 
        'image': recipe.image,
    }
    return render(request, 'home_recipe.html', context)
