# Generated by Django 2.1.7 on 2019-04-18 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20190416_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placeinfo',
            name='guestRoomReferencePrice',
        ),
        migrations.RemoveField(
            model_name='placeinfo',
            name='minMealCost',
        ),
    ]
