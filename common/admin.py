from django.contrib import admin

from common.models import MuscleGroupMixin


@admin.register(MuscleGroupMixin)
class MuscleGroupMixinAdmin(admin.ModelAdmin):
    list_display = ('group_name',)
