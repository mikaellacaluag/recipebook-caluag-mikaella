from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(
        validators=[
            MinLengthValidator(255, "the field must contain at least 255 characters")
        ]
    )


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ledger:ingredient_detail", args=[self.pk])

    class Meta:
        ordering = ["name"]
        verbose_name = "ingredient"
        verbose_name_plural = "ingredients"


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="recipes"
    )
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ledger:recipe-detail", args=[str(self.pk)])

    class Meta:
        ordering = ["name"]
        verbosename = "recipe"
        verbose_name_plural = "recipes"


class RecipeIngredient(models.Model):
    quantity = models.IntegerField()

    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="recipe"
    )

    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients"
    )

    def __str__(self):
        return "{} {} for {}".format(self.quantity, self.ingredient, self.recipe)

    class Meta:
        ordering = ["recipe", "ingredient"]
        verbose_name = "recipe ingredient"
        verbose_name_plural = "recipe ingredients"
        unique_together = ("recipe", "ingredient")
