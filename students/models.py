from django.db import models
from courses.models import Course


class Student(models.Model):
    PACKAGE_CHOICE = (
        ('S', 'Standart'),
        ('G', 'Gold'),
        ('V', 'VIP'),
    )

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course = models.ForeignKey(Course, blank=True)
    package_choice = models.CharField(max_length=1, 
                                      choices=PACKAGE_CHOICE, default='S')
    
    def __unicode__(self):
        return "%s %s" %(self.name, self.surname)