from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Recipe, Ingredient
from .forms import IngredientSearchForm

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"
    context_object_name = "recipes"

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"
    context_object_name = "recipe"

def search_recipes(request):
    if request.method == "GET":
        form = IngredientSearchForm(request.GET)
        if form.is_valid():
            ingredients_input = form.cleaned_data['ingredients']
            ingredients = [i.strip() for i in ingredients_input.split(',')]
            recipes = Recipe.objects.filter(ingredients__name__in=ingredients).distinct()
            return render(request, 'recipes/search_results.html', {'recipes': recipes, 'form': form})
    else:
        form = IngredientSearchForm()
    return render(request, 'recipes/search.html', {'form': form})