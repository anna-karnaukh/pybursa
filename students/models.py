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
    courses = models.ManyToManyField(Course, blank=True, null=True)
    package_choice = models.CharField(max_length=1, 
                                      choices=PACKAGE_CHOICE, default='S')
    dossier = models.OneToOneField('students.Dossier', blank=True, null=True)
    
    def __unicode__(self):
        return "%s %s" %(self.name, self.surname)


class Address(models.Model):
    postcode = models.CharField(max_length=5)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house = models.CharField(max_length=5)

    def __unicode__(self):
        return "%s, %s, %s, %s, %s" % (self.postcode, self.country, self.city,
                                 self.street, self.house)


class Dossier(models.Model):
    COLORS = (('r', 'red'),
              ('o', 'orange'),
              ('y', 'yellow'),
              ('g', 'green'),
              ('b', 'blue'),
              ('v', 'violet')
             )
    address = models.ForeignKey('students.Address', blank=True, null=True)
    unliked_courses = models.ManyToManyField(Course, blank=True,
                                             null=True)
    favourite_color = models.CharField(max_length=1, choices=COLORS,
                                       default='r')

    def __unicode__(self):
        return "%s" % self.id
