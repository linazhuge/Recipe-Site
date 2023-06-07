from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.selectr_view, name='select'),
    path('showall', views.showall_view, name='showall'),
    re_path('edit/^(?P<pk>\d+)', views.edit_view, name='edit'),
    re_path('delete/^(?P<pk>\d+)', views.delete_view, name='delete'),
    re_path('viewrecipe/^(?P<pk>\d+)', views.recipe_view, name='view_recipe')
]
