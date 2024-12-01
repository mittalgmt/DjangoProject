from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render, get_object_or_404
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
    # Separate view for adding an ingredient (if needed in the UI)
    if request.method == 'POST':
        ingredient_name = request.POST.get('ingredient_name')
        if ingredient_name:
            Ingredient.objects.get_or_create(name=ingredient_name.strip())
        return redirect('add_recipe')  # Redirect to the add_recipe view
    return render(request, 'recipes/add_ingredient.html')

def add_recipe(request):
    if request.method == 'POST':
        # Create RecipeForm instance
        recipe_form = RecipeForm(request.POST, request.FILES)

        if recipe_form.is_valid():
            recipe = recipe_form.save()  # Save recipe

            # Handle existing ingredients
            existing_ingredients = request.POST.getlist('existing_ingredients')
            for ingredient_id in existing_ingredients:
                if ingredient_id:  # Check for valid ingredient ID
                    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
                    recipe.ingredients.add(ingredient)

            # Handle new ingredient
            new_ingredient = request.POST.get('new_ingredient')
            if new_ingredient:  # Add a new ingredient if provided
                ingredient_obj, created = Ingredient.objects.get_or_create(name=new_ingredient.strip())
                recipe.ingredients.add(ingredient_obj)

            return redirect('recipe_detail', pk=recipe.pk)  # Redirect to recipe detail
    else:
        recipe_form = RecipeForm()
        ingredients = Ingredient.objects.all()  # Pass existing ingredients for dropdown

    return render(request, 'recipes/add_recipe.html', {'recipe_form': recipe_form, 'ingredients': ingredients})
