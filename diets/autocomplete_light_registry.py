import autocomplete_light.shortcuts as al
from diets.models import Meal

al.register(Meal,

    search_fields=['food_group', 'food'],
    attrs={
         'placeholder': 'Food group or food',
         'data-autocomplete-minimum-characters': 1,
     },

    widget_attrs={
        'data-widget-maximum-values': 4,
        'class': 'modern-style',
     },
)