from django.contrib import admin
from workouts.models import MuscleGroup, Workout, Exercise, ExerciseSet


# class ExerciseSetInline(admin.TabularInline):
#     model = ExerciseSet
#     raw_id_fields = ('exercise', )
#     list_display = ('exercise', 'number_of_sets', 'weight', 'reps', 'notes', )


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    search_fields = ('workout_name', )
    list_display = ('workout_name', 'group_name',)
    list_filter = ('group_name',)
    filter_horizontal = ('exercise', )


@admin.register(ExerciseSet)
class ExerciseSetAdmin(admin.ModelAdmin):
    list_display = ('exercise','number_of_sets', 'weight', 'reps', 'notes',)
    list_filter = ('group_name',)
    # search_fields = ('reps',)
    # raw_id_fields = ('exercise',)


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('group_name',)
    # list_display = ('name', 'group_name',)

admin.site.register(MuscleGroup)




