from django.db import models

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50)
    
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)

class RecipeIngredients(models.Model):
    quantity = models.IntegerField()

    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE, 
        related_name="ingredients"
    )

    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE, 
        related_name = "recipes"
    )