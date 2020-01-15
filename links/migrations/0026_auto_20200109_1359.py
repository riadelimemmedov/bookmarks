# Generated by Django 2.2.7 on 2020-01-09 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0025_auto_20200109_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movebookmark',
            name='dest_collection',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='links.Collection'),
        ),
        migrations.AlterField(
            model_name='movebookmark',
            name='dest_page',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='links.Page'),
        ),
    ]