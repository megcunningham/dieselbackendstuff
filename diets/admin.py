from django.contrib import admin

from diets.models import ClientStat, FoodGroup, Food, Meal, Diet, MeasureServing, Quantity

#
# admin.site.register(MeasureServing)
# admin.site.register(Quantity)
# @admin.register(MeasureServing)
# class MeasureServingAdmin(admin.ModelAdmin):
#     list_display = ('serving_size',)
#     fields = ('serving_size',)


class ClientStatInline(admin.StackedInline):
    model = ClientStat
    extra = 0


@admin.register(ClientStat)
class ClientStatAdmin(admin.ModelAdmin):
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"
    list_display = ('name', 'body_fat', 'weight', 'show', 'weeks_out', 'date',)
    list_filter = ('name', 'show', 'weeks_out',)
    search_fields = ('name', 'show', 'weeks_out',)


@admin.register(FoodGroup)
class FoodGroupAdmin(admin.ModelAdmin):
    list_display = ('food_group',)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"
    search_fields = ('food',)
    list_display = ('food', 'food_group',)
    list_filter = ('food_group',)


class MealInline(admin.TabularInline):
    model = Meal
    fields = ('note', 'food', 'quantity', 'serving_size',)
    extra = 5
    max_num = 30
    raw_id_fields = ('food',)
    classes = ('grp-collapse grp-open',)
    # define the related_lookup_fields
    related_lookup_fields = {
        'fk': ['food_group'],
    }


# class MealNumberInline(admin.TabularInline):
#     model = MealNumber
#     inlines = [MealInline,]
#     fields = ('meal_number', 'food', 'quantity', 'serving_size',)
#     max_num = 7


@admin.register(Diet)
class DietAdmin(admin.ModelAdmin):
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"
    inlines = [MealInline,]
    fields = ('date', 'name', 'weight', 'body_fat', 'show', 'weeks_out', )
    list_display = ('date', 'name', 'weight', 'body_fat',)
    search_fields = ('name', 'date',)
    list_filter = ('name',)













