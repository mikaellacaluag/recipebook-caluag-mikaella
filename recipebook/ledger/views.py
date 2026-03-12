from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Recipe, RecipeImage
from django.contrib. auth.decorators import login_required

def index(request):
    return HttpResponse('Welcome to the Ledger App!')

def recipes(request):
    
    recipes = Recipe.objects.all()

    return render(request, "ledger/recipes.html", {
        "recipes": recipes,
    })

@login_required
def recipe(request, id):

    recipe = Recipe.objects.get(id=id)

    return render(request, "ledger/recipe.html", {
        "recipe": recipe,
    })

@login_required
def add_recipe(request):

    if request.method == "POST":
        name = request.POST.get("name")

        if name:
            recipe = Recipe.objects.create(
                name=name,
                author=request.user.profile
            )

            return redirect(recipe.get_absolute_url())

    return render(request, "ledger/add_recipe.html")

def recipe_forms(request, id):
    recipe = Recipe.objects.get(id=id)

    if request.method == "POST":
        image = request.FILES.get("recipe_image")
        description = request.POST.get("description")

        if image and description:
            RecipeImage.objects.create(
                recipe=recipe, recipe_image=image, description=description
            )
            return redirect(recipe.get_absolute_url())
        
    return render(request, "ledger/add_image.html",{
        "recipe": recipe,
    })
        

