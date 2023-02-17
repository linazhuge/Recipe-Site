from django.urls import path
from . import views

urlpatterns = [
    path('', views.selectr_view, name='select'),
    path('showall', views.showall_view, name='showall'),
    path('edit/^(?P<pk>\d+)', views.edit_view, name='edit'),
    path('viewrecipe/^(?P<pk>\d+)', views.recipe_view, name='view_recipe')
]
