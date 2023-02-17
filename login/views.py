from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def home_view(request):
    #context ={}
    #form = InputForm(request.POST or None, request.FILES or None)

    #if form.is_valid():
    #    form.save()
    
    #context['form'] = form
    #return render(request, "home.html", context)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('valid')
        else:
            print('invalid')

    else:
        form = UserCreationForm()
    context = {
        'form': form
    }

    return render(request, 'home.html', context)

def recipe_view(request):
    context = {

    }
    return render(request, 'recipe_view.html', context)