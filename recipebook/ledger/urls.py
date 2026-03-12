from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', recipes, name="recipe-list"),
    path('recipe/<int:id>/', recipe, name='recipe-detail'),
    path('recipe/<int:id>/add-image/', recipe_forms, name="recipe_forms"),
]

app_name = "ledger"