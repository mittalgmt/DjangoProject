from django import forms
from .models import Ingredient

class IngredientSearchForm(forms.Form):
    ingredients = forms.CharField(
        label="Enter ingredients (comma-separated)",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., tomato, onion, garlic'})
    )
