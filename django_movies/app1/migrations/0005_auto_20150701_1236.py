# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20150630_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movie',
        ),
        migrations.AddField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(default=0, to='app1.Movie'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.CharField(max_length=200, default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_title',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rater',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rater',
            name='gender',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='rater',
            name='occupation',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rater',
            name='user',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(to='app1.Rater'),
        ),
    ]
