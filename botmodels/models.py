from django.db import models

class Dish(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    picture = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

class DishProduct(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)

class DishStep(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    order = models.IntegerField()
    description = models.TextField(blank=True, null=True)