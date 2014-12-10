# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_name'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('postcode', models.CharField(max_length=5)),
                ('country', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('house', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('favourite_color', models.CharField(default=b'r', max_length=1, choices=[(b'r', b'red'), (b'o', b'orange'), (b'y', b'yellow'), (b'g', b'green'), (b'b', b'blue'), (b'v', b'violet')])),
                ('address', models.ForeignKey(blank=True, to='students.Address', null=True)),
                ('unliked_courses', models.ManyToManyField(to='courses.Course', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='courses.Course', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='dossier',
            field=models.OneToOneField(null=True, blank=True, to='students.Dossier'),
            preserve_default=True,
        ),
    ]
