from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50)

    def __str__(self):
        return self.ingredient_name
    
    def get_absolute_url(self):
        return reverse('recipe', args=[str(self.pk)])
    
    class Meta:
        ordering = ['ingredient_name']
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)

    def __str__(self):
        return self.recipe_name
    
    def get_absolute_url(self):
        return reverse('recipes', args=[str(self.pk)])
    
    class Meta:
        ordering = ['recipe_name']
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'

class RecipeIngredient(models.Model):
    quantity = models.IntegerField()

    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE, 
        related_name="recipe_ingredients"
    )

    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE, 
        related_name = "recipe_ingredients"
    )

    def __str__(self):
        return '{} {} for {}'.format(self.quantity, self.ingredient, self.recipe)
    
    class Meta:
        ordering = ['recipe', 'ingredient']
        verbose_name = 'recipe ingredient'
        verbose_name_plural = 'recipe ingredients'
        unique_together = ('recipe', 'ingredient')
    
    

    
