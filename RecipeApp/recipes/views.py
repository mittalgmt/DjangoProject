from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render
from .models import Recipe, Ingredient
from .forms import IngredientSearchForm, RecipeForm

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


def add_ingredient(request):
    return render(request, 'recipes/add_ingredient.html')


def add_recipe(request):
    if request.method == 'POST':
        # Create RecipeForm instance
        recipe_form = RecipeForm(request.POST, request.FILES)
        
        if recipe_form.is_valid():
            recipe = recipe_form.save()  # Save recipe

            # Handle ingredients
            ingredients = request.POST.getlist('ingredients')
            for ingredient_name in ingredients:
                ingredient = Ingredient.objects.create(name=ingredient_name)
                recipe.ingredients.add(ingredient) 
                
            return redirect('recipe_detail', pk=recipe.id)
    else:
        recipe_form = RecipeForm()

    return render(request, 'recipes/add_recipe.html', {'recipe_form': recipe_form})