from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', recipes, name="recipe-list"),
    path('recipe/<int:id>/', recipe, name='recipe-detail')

]

app_name = "ledger"