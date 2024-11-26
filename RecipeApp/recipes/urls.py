from django.urls import path
from .views import RecipeListView, RecipeDetailView, search_recipes

urlpatterns = [
    path('', search_recipes, name='search_recipes'),
    path('recipes/', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
]
