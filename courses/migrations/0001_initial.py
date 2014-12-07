# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('technology_choice', models.CharField(default=b'P', max_length=1, choices=[(b'P', b'Python'), (b'R', b'Ruby'), (b'J', b'JavaScript')])),
                ('description', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('assistant', models.ForeignKey(related_name='assistant', to='coaches.Coach')),
                ('teacher', models.ForeignKey(to='coaches.Coach')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
