from django import forms
from .models import Recipe,Ingredient

class IngredientSearchForm(forms.Form):
    ingredients = forms.CharField(
        label="Enter ingredients (comma-separated)",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., tomato, onion, garlic'})
    )


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'image', 'instructions']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']
