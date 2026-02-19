from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

def index(request):
    return HttpResponse('Welcome to the Ledger App!')

def recipes(request):
    
    recipes = Recipe.objects.all()

    return render(request, "ledger/recipes.html", {
        "recipes": recipes,
    })

def recipe(request, id):

    recipe = Recipe.objects.get(id=id)

    return render(request, "ledger/recipe.html", {
        "recipe": recipe,
    })