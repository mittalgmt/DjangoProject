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

        if self.image:
            img_path = self.image.path
            img = Image.open(img_path)

            # Resize image
            output_size = (200, 200)  # Desired dimensions
            img = img.resize(output_size, Image.ANTIALIAS)
            img.save(img_path)  # Save resized image


class UserFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.recipe.title}"