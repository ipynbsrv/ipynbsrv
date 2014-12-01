# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wui', '0002_auto_20141201_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageshare',
            name='gid',
            field=models.ForeignKey(blank=True, to='wui.Group', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imageshare',
            name='uid',
            field=models.ForeignKey(blank=True, to='wui.User', null=True),
            preserve_default=True,
        ),
    ]