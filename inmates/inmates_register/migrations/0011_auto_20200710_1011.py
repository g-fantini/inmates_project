# Generated by Django 3.0 on 2020-07-10 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmates_register', '0010_auto_20200710_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='location',
            field=models.CharField(choices=[('1', 'Cell'), ('2', 'Garden'), ('3', 'Cafeteria'), ('4', 'Shower'), ('5', 'kitchen')], max_length=15),
        ),
    ]