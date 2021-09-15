from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=32)              # ex. "flour"
    quantity = models.FloatField(default=0.0)           # ex. 4.5
    unit = models.CharField(max_length=16)              # ex. "tbsp"
    unit_price = models.FloatField(default=0.0)         # ex. 0.05

    def __str__(self):
        return self.name

    def cost(self):
        # TODO: we want to return quantity * unit_price, but how do we access
        # those values from the fields?
        # return self.unit_price.as_float() * self.quantity.as_float()
        return 0.0


class MenuItem(models.Model):
    title = models.CharField(max_length=64)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.title


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)           # ex. 4.5


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
