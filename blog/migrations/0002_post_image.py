# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=datetime.datetime(2015, 12, 17, 19, 31, 52, 790100, tzinfo=utc), upload_to='images/art/'),
            preserve_default=False,
        ),
    ]
