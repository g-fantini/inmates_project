# Generated by Django 3.0 on 2020-07-09 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmates_register', '0003_auto_20200709_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='location',
            field=models.CharField(choices=[{'kitchen', 'KT'}, {'Cell', 'CL'}, {'CF', 'Cafeteria'}, {'GR', 'Garden'}, {'Shower', 'SH'}], max_length=15),
        ),
    ]