from django.contrib import admin
from students.models import Student, Address, Dossier


admin.site.register(Student)
admin.site.register(Address)
admin.site.register(Dossier)
