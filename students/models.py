from django.db import models
from django.utils.translation import ugettext_lazy as _
from courses.models import Course


class Student(models.Model):
    PACKAGE_CHOICE = (
        ('S', 'Standart'),
        ('G', 'Gold'),
        ('V', 'VIP'),
    )

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    surname = models.CharField(max_length=255, verbose_name=_("Surname"))
    date_of_birth = models.DateField(verbose_name=_("Date of birth"))
    email = models.EmailField(verbose_name=_("Email"))
    phone = models.CharField(max_length=15, verbose_name=_("Phone"))
    courses = models.ManyToManyField(Course, blank=True, null=True,
                                     verbose_name=_("Courses"))
    package_choice = models.CharField(max_length=1, 
                                      choices=PACKAGE_CHOICE, default='S',
                                      verbose_name=_("Package"))
    dossier = models.OneToOneField('students.Dossier', blank=True, null=True,
                                    verbose_name=_("Dossier"))
    
    def __unicode__(self):
        return "%s %s" %(self.name, self.surname)


class Address(models.Model):
    postcode = models.CharField(max_length=5, verbose_name=_("Postcode"))
    country = models.CharField(max_length=50, verbose_name=_("Country"))
    region = models.CharField(max_length=255, verbose_name=_("Region"))
    city = models.CharField(max_length=255, verbose_name=_("City"))
    district = models.CharField(max_length=255, verbose_name=_("District"))
    street = models.CharField(max_length=255, verbose_name=_("Sstreet"))
    house = models.CharField(max_length=5, verbose_name=_("House"))

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
    address = models.ForeignKey('students.Address', blank=True, null=True,
                                verbose_name=_("Address"))
    unliked_courses = models.ManyToManyField(Course, blank=True,
                                             null=True,
                                             verbose_name=_("Unliked courses"))
    favourite_color = models.CharField(max_length=1, choices=COLORS,
                                       default='r', 
                                       verbose_name=_("Favourite color"))

    def __unicode__(self):
        return "%s" % self.id
