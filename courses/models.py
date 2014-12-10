from django.db import models
from coaches.models import Coach

class Course(models.Model):
    TECHNOLOGY_CHOICE = (
        ('P', 'Python'),
        ('R', 'Ruby'),
        ('J', "JavaScript"),
    )

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    teacher = models.ForeignKey(Coach, limit_choices_to={'coach_type': 'T'})
    assistant = models.ForeignKey(Coach, limit_choices_to={'coach_type': 'A'}, 
        related_name="assistant")
    start_date = models.DateField()
    end_date = models.DateField()
    technology_choice = models.CharField(max_length=1, 
                                         choices=TECHNOLOGY_CHOICE, 
                                         default='P')
    venue = models.ForeignKey('students.Address', null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.get_technology_choice_display()
