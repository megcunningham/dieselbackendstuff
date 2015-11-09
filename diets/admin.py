from django.contrib import admin

from diets.models import Stat, Food, Meal, Serving, Protein, Carbohydrate, Green, NewDiet, Fat


admin.site.register(Meal)
admin.site.register(Serving)
admin.site.register(Protein)
admin.site.register(Carbohydrate)
admin.site.register(Green)
admin.site.register(Fat)
admin.site.register(NewDiet)


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('name', 'body_fat', 'weight', 'show', 'weeks_out',)
    list_filter = ('name', 'show', 'weeks_out',)
    search_fields = ('name', 'show', 'weeks_out',)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    raw_id_fields = ('protein', 'carbohydrates', 'greens', 'fats',)
    list_filter = ('protein', 'carbohydrates', 'greens', 'fats',)





