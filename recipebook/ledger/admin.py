from django.contrib import admin

from .models import Recipe, RecipeIngredient

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

admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
