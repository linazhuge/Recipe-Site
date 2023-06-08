from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.selectr_view, name='select'),
    path('showall/', views.showall_view, name='showall'),
    path('edit/<int:pk>/', views.edit_view, name='edit'),
    path('delete/<int:pk>/', views.delete_view, name='delete'),
    path('viewrecipe/<int:pk>/', views.recipe_view, name='view_recipe')
]
