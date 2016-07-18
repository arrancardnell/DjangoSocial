# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_auto_20160607_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('user_from', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='rel_from_set')),
                ('user_to', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='rel_to_set')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
