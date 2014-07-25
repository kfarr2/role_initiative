# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from south.db import db 
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('name', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('char_class', models.CharField(max_length=50)),
                ('char_skills', models.TextField()),
                ('char_story', models.TextField()),
                ('brawn', models.IntegerField(default=1)),
                ('finesse', models.IntegerField(default=1)),
                ('wits', models.IntegerField(default=1)),
                ('resolve', models.IntegerField(default=1)),
                ('panache', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
