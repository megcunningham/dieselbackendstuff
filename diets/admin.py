from django.contrib import admin

from diets.models import ClientStat, FoodGroup, Food, Meal, Diet, MeasureServing


class ClientStatInline(admin.StackedInline):
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
    # raw_id_fields = ('protein', 'carbohydrates', 'greens', 'fats',)
    search_fields = ('food',)
    list_display = ('food', 'food_group',)
    list_filter = ('food_group',)


class MealInline(admin.StackedInline):
    model = Meal


class MeasureServingInline(admin.TabularInline):
    model = MeasureServing
    fieldsets = [food, serving_size,]


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    inlines = [MeasureServingInline,]


@admin.register(Diet)
class DietAdmin(admin.ModelAdmin):
    inlines = [MealInline,]



#
#
# class MeasureServingInline(admin.TabularInline):
#     model = MeasureServing
#     extra = 3
#     max_num = 3
#
#
# @admin.register(NewDiet)
# class NewDietAdmin(admin.ModelAdmin):
#     inlines = [MeasureServingInline,]







