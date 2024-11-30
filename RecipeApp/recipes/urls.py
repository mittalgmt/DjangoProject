from django.urls import path
from .views import RecipeListView, RecipeDetailView, search_recipes
from  recipes import views

urlpatterns = [
    path('', search_recipes, name='search_recipes'),
    path('recipes/', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('add_ingredient/', views.add_ingredient, name='add_ingredient'),
]
