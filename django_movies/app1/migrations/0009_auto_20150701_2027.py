from __future__ import unicode_literals
from django.db import models, migrations
import pandas as pd
from app1.models import Rater


def load_raters(apps, schema_editor):
    rater_data = pd.read_csv('ml-1m/users.dat', names=["id", "gender", "age","occupation","postal_code"], encoding="windows-1252", sep="::")
    for rater in rater_data.iterrows():
        rater_obj = rater[1]
        Rater.objects.create(id=rater_obj.id,
                             gender=rater_obj.gender,
                             age=rater_obj.age,
                             occupation=rater_obj.occupation,
                             postal_code=rater_obj.postal_code)


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_remove_rater_user'),
    ]

    operations = [
        migrations.RunPython(load_raters)
    ]
