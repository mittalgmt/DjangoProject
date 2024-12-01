from django import forms
from .models import Recipe,Ingredient

class IngredientSearchForm(forms.Form):
    ingredients = forms.CharField(
        label="Enter ingredients (comma-separated)",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., tomato, onion, garlic'})
    )



class RecipeForm(forms.ModelForm):
    new_ingredient = forms.CharField(
        max_length=100,
        required=False,
        label="Add New Ingredient",
        help_text="Enter a new ingredient if not available in the dropdown."
    )
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Select Ingredients"
    )

    class Meta:
        model = Recipe
        fields = ['title', 'image', 'ingredients', 'instructions', 'new_ingredient']

    def clean_new_ingredient(self):
        new_ingredient = self.cleaned_data.get('new_ingredient')
        if new_ingredient and Ingredient.objects.filter(name=new_ingredient).exists():
            raise forms.ValidationError(f"The ingredient '{new_ingredient}' already exists.")
        return new_ingredient

    

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']
