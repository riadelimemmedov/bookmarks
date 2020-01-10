# Generated by Django 2.2.7 on 2020-01-10 13:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0027_auto_20200110_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='num_of_columns',
            field=models.PositiveIntegerField(default=4, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
