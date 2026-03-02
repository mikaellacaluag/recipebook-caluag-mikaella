from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Recipe, RecipeIngredient, Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline, ]


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

    search_fields = ('recipe', )

    list_display = ('ingredient', 'quantity', 'recipe')

    list_filter = ('recipe', )

    fieldsets = [
        ('Details',{
            'fields': [
                ('ingredient', 'quantity'), 'recipe'
            ]
        })
    ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
