from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Recipe, Ingredient, RecipeIngredient

def index(request):
    return HttpResponse('Welcome to the Ledger App!')

def recipes(request):
    
    recipes = Recipe.objects.all()

    return render(request, "ledger/recipes.html", {
        "recipes": recipes,
    })

def recipe(request, id):

    recipe = Recipe.objects.get(pk=id)

    return render(request, "ledger/recipe.html", {
        "recipe": recipe,
    })

class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipes.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'ledger/recipe.html'
