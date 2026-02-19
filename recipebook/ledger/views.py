from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Ingredient, RecipeIngredient


def index(request):
    return HttpResponse('Welcome to the Ledger App!')

def recipes(request):
    
    recipe = Recipe.objects.get(pk=id)

    return render(request, "ledger/recipes.html", {
        "recipe": recipe,
    })

def recipe(request, id):

    ingredients = Ingredient.objects.get(pk=id)

    return render(request, "ledger/recipe.html", {
        "ingredients": ingredients
    })
    