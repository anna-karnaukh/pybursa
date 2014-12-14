from django.contrib import admin
from courses.models import Course


class CourseAdmin(admin.ModelAdmin):
    if len(Course.TECHNOLOGY_CHOICE) < 5:
        radio_fields = {'technology_choice': admin.HORIZONTAL}
    list_display = ['name', 'technology_choice', 'start_date', 'end_date']
    list_filter = ['start_date', 'end_date', 'technology_choice']
    list_display_links = ['name', 'technology_choice']
    list_editable = ['start_date', 'end_date']
    search_fields = ['name', 'technology_choice', 'start_date', 'end_date']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['start_date', 'end_date', 'name']


admin.site.register(Course, CourseAdmin)
