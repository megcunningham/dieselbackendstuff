from django.contrib import admin
from workouts.models import Workout, ExerciseName, CompleteSet, DifficultyLevel, WeeklyWorkout, Split, \
    NumberOfSet



@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    search_fields = ('workout_name', )
    list_display = ('workout_name', 'group_name', 'level',)
    list_filter = ('group_name', 'level', )
    filter_horizontal = ('exercise', )


class NumberOfSetInline(admin.TabularInline):
    model = NumberOfSet
    list_display = ('set_number', 'reps', 'weight',)


@admin.register(CompleteSet)
class CompleteSetAdmin(admin.ModelAdmin):
    inlines = [NumberOfSetInline,]
    # raw_id_fields = ('exercise',)
    list_display = ('exercise',)
    search_fields = ('exercise',)
    # list_filter = ('group_name',)


# @admin.register(ExerciseSet)
# class ExerciseSetAdmin(admin.ModelAdmin):
#     list_display = ('exercise', 'notes',)
#     raw_id_field = ('exercise', )
#     list_filter = ('group_name',)


@admin.register(ExerciseName)
class ExerciseNameAdmin(admin.ModelAdmin):
    search_fields = ('name',)

    list_filter = ('group_name',)
    list_display = ('name', 'group_name',)


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



admin.site.register(DifficultyLevel)




