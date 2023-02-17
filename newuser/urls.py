from django.urls import path
from . import views

urlpatterns = [
    path('', views.newuser_view, name='newuser'),
]