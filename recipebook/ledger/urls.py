from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', recipes, name="recipes"),
    path('recipe/<int:id>/', recipe, name='recipe')

]

app_name = "ledger"