# Generated by Django 3.0 on 2020-07-13 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmates_register', '0015_auto_20200713_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='car',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='company',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
