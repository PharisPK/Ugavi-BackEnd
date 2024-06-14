# Generated by Django 5.0.6 on 2024-06-14 02:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fieldmapping', '0008_alter_farm_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='produce',
            field=models.ManyToManyField(related_name='farms', to='fieldmapping.produce'),
        ),
        migrations.AlterField(
            model_name='location',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2024, 6, 14, 2, 40, 40, 187303, tzinfo=datetime.timezone.utc)),
        ),
    ]
