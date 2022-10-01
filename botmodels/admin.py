from django.contrib import admin
from .models import Dish, DishStep, DishProduct

class DishStepInline(admin.TabularInline):
    model = DishStep

class DishProductsInline(admin.TabularInline):
    model = DishProduct


class DishAdmin(admin.ModelAdmin):
    inlines = [
        DishStepInline,
        DishProductsInline,
    ]


admin.site.register(Dish, DishAdmin)
