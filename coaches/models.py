from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Coach(models.Model):
    COACH_TYPES = (('T', _('Teacher')), ('A', _('Assistant')),)

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    surname = models.CharField(max_length=255, verbose_name=_("Surname"))
    email = models.EmailField(verbose_name=_("Email"))
    phone = models.CharField(max_length=15, verbose_name=_("Phone"))
    coach_type = models.CharField(max_length=1, choices=COACH_TYPES, 
                                  verbose_name=_("Coach_type"))
    course_name = models.CharField(max_length=255, 
                                   verbose_name=_("Course_name"))
    user = models.ForeignKey(User, verbose_name=_("User"))
    dossier = models.OneToOneField('students.Dossier', blank=True, null=True, 
                                   verbose_name=_("Dossier"))
    
    def __unicode__(self):
        return "%s %s" %(self.name, self.surname)
