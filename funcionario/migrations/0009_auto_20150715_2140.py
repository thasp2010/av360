# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0008_auto_20150715_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='usuarioFunc',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
