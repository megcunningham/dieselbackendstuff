from django.contrib import admin
from workouts.models import MuscleGroup, Workout, ExerciseName, ExerciseSet, DifficultyLevel, WeeklyWorkout, Split

# admin.site.register(Split)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    # inlines = [AddWorkoutInline,]
    search_fields = ('workout_name', )
    list_display = ('workout_name', 'group_name', 'level',)
    list_filter = ('group_name', 'level', )
    filter_horizontal = ('exercise', )


@admin.register(ExerciseSet)
class ExerciseSetAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'number_of_sets', 'weight', 'reps', 'notes',)
    list_filter = ('group_name',)
    # search_fields = ('reps',)
    # raw_id_fields = ('exercise',)


@admin.register(ExerciseName)
class ExerciseNameAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('group_name',)
    # list_display = ('name', 'group_name',)


class SplitInline(admin.StackedInline):
    model = Split
    extra = 3
    max_num = 3
    filter_horizontal = ('workouts',)
    # list_display = ('day', 'workouts.workout_name',)


@admin.register(WeeklyWorkout)
class WeeklyWorkoutAdmin(admin.ModelAdmin):
    # list_display = ('week_of',)
    inlines = [SplitInline,]


admin.site.register(MuscleGroup)
admin.site.register(DifficultyLevel)




