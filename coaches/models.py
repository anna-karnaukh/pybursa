from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    COACH_TYPES = (('T', 'Teacher'), ('A', 'Assistant'),)

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    coach_type = models.CharField(max_length=1, choices=COACH_TYPES)
    course_name = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    dossier = models.OneToOneField('students.Dossier', blank=True, null=True)
    
    def __unicode__(self):
        return "%s %s" %(self.name, self.surname)
