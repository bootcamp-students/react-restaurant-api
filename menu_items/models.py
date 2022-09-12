from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

class Cuisine(models.Model):
    label = models.CharField(max_length=200)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name_plural = "Cusines"

class Item(models.Model):
    category = models.ForeignKey(Category, related_name="category_label", on_delete=models.CASCADE, null=True, blank=True)
    cuisine = models.ForeignKey(Cuisine, related_name="cuisine_label", on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    spicy_level = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.title
