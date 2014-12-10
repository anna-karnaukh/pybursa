# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20141210_1908'),
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='dossier',
            field=models.OneToOneField(null=True, blank=True, to='students.Dossier'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coach',
            name='phone',
            field=models.CharField(default=9379992, max_length=15),
            preserve_default=False,
        ),
    ]
