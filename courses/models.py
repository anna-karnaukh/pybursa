from django.db import models
from django.utils.translation import ugettext_lazy as _
from coaches.models import Coach

class Course(models.Model):
    TECHNOLOGY_CHOICE = (
        ('P', 'Python'),
        ('R', 'Ruby'),
        ('J', "JavaScript"),
    )

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.CharField(max_length=255, verbose_name=_("Description"))
    teacher = models.ForeignKey(Coach, limit_choices_to={'coach_type': 'T'},
                                verbose_name=_("Coach"))
    assistant = models.ForeignKey(Coach, limit_choices_to={'coach_type': 'A'}, 
        related_name="assistant", verbose_name=_("Assistant"))
    start_date = models.DateField(verbose_name=_("Start date"))
    end_date = models.DateField(verbose_name=_("End date"))
    technology_choice = models.CharField(max_length=1, 
                                         choices=TECHNOLOGY_CHOICE, 
                                         default='P',
                                         verbose_name=_("Technology choice"))
    venue = models.ForeignKey('students.Address', null=True, blank=True,
                              verbose_name=_("Venue"))
    slug = models.SlugField(max_length=255, blank=True, default="",
                            verbose_name=_("Slug"))

    def __unicode__(self):
        return "%s" % self.get_technology_choice_display()
