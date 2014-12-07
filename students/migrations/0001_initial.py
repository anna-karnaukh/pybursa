# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=15)),
                ('package_choice', models.CharField(default=b'S', max_length=1, choices=[(b'S', b'Standart'), (b'G', b'Gold'), (b'V', b'VIP')])),
                ('course', models.ForeignKey(to='courses.Course', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
