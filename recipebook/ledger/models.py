from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recipe-list')
    
    class Meta:
        ordering = ['name']
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'

class Recipe(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recipe-detail', args=[str(self.pk)])
    
    class Meta:
        ordering = ['name']
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'

class RecipeIngredient(models.Model):
    quantity = models.IntegerField()

    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE, 
        related_name="recipe"
    )

    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE, 
        related_name = "ingredients"
    )

    def __str__(self):
        return '{} {} for {}'.format(self.quantity, self.ingredient, self.recipe)
    
    class Meta:
        ordering = ['recipe', 'ingredient']
        verbose_name = 'recipe ingredient'
        verbose_name_plural = 'recipe ingredients'
        unique_together = ('recipe', 'ingredient')
    
    

    
