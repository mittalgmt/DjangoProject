from django.contrib import admin
from .models import Recipe, Ingredient

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('ingredients',)  
