from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipes/',blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
           output_size = (300, 300)
           img = img.resize(output_size, Image.Resampling.LANCZOS)  # Updated line
           img.save(self.image.path)

     
class UserFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.recipe.title}"