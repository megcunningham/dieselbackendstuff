from django.contrib import admin

from diets.models import ClientStat, FoodGroup, Food, Meal, Diet, MeasureServing, Quantity, MealNumber


# @admin.register(MeasureServing)
# class MeasureServingAdmin(admin.ModelAdmin):
#     list_display = ('serving_size',)
#     fields = ('serving_size',)

class ClientStatInline(admin.TabularInline):
    model = ClientStat
    extra = 0


@admin.register(ClientStat)
class ClientStatAdmin(admin.ModelAdmin):
    list_display = ('name', 'body_fat', 'weight', 'show', 'weeks_out',)
    list_filter = ('name', 'show', 'weeks_out',)
    search_fields = ('name', 'show', 'weeks_out',)


@admin.register(FoodGroup)
class FoodGroupAdmin(admin.ModelAdmin):
    list_display = ('food_group',)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    search_fields = ('food',)
    list_display = ('food', 'food_group',)
    list_filter = ('food_group',)


class MealInline(admin.TabularInline):
    model = Meal
    fields = ('food', 'quantity', 'serving_size',)
    extra = 4
    max_num = 5


class MealNumberInline(admin.TabularInline):
    model = MealNumber
    inlines = [MealInline,]
    fields = ('meal_number', 'food', 'quantity', 'serving_size',)
    max_num = 7

@admin.register(Diet)
class DietAdmin(admin.ModelAdmin):
    inlines = [MealNumberInline, MealInline]
    # raw_id_fields = ('client',)
    fields = ('date', 'name', 'weight', 'body_fat', 'show', 'weeks_out', )
    list_display = ('date', 'name',)
    search_fields = ('name', 'date',)
    list_filter = ('name',)










