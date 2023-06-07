from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('recipe', views.home_view_recipe, name='home_recipe')
]
