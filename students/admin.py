from django.contrib import admin
from students.models import Student, Address, Dossier


class StudentAdmin(admin.ModelAdmin):
    if len(Student.PACKAGE_CHOICE) < 5:
        radio_fields = {'package_choice': admin.HORIZONTAL}
    list_display = ['name', 'surname', 'package_choice']
    list_filter = ['package_choice',]
    list_editable = ['package_choice',]
    search_fields = (
'name', 'surname', 'courses', 'email', 'phone', 'package_choice')
    filter_vertical = ['courses',]


class AddressAdmin(admin.ModelAdmin):
    list_display = ['postcode', 'country', 'city', 'street', 'house']
    list_filter = ['country', 'city', 'street']
    search_fields = ['postcode', 'country', 'city', 'street', 'house']


class DossierAdmin(admin.ModelAdmin):
    if len(Dossier.COLORS) < 5:
        radio_fields = {'favourite_color': admin.VERTICAL}
    list_display = ['address', 'favourite_color']
    list_filter = ['favourite_color',]
    list_display_links = ['address']
    search_fields = ['favourite_color']
    filter_horizontal = ['unliked_courses', ]
    ordering = ['favourite_color']


admin.site.register(Student, StudentAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Dossier, DossierAdmin)
