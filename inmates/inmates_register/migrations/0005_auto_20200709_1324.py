# Generated by Django 3.0 on 2020-07-09 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmates_register', '0004_auto_20200709_1315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inmate',
            old_name='dude',
            new_name='history',
        ),
    ]
