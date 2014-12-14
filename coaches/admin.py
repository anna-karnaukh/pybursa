from django.contrib import admin
from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    if len(Coach.COACH_TYPES) < 5:
        radio_fields = {'coach_type': admin.HORIZONTAL}
    list_display = ('name', 'surname', 'coach_type')
    list_filter = ['coach_type', ]
    list_editable = ['coach_type', ]
    search_fields = ('name', 'surname', 'coach_type', 'email', 'phone')
    ordering = ['name']


admin.site.register(Coach, CoachAdmin)
