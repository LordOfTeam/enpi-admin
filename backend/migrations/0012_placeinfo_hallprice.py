# Generated by Django 2.1.7 on 2019-04-21 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_auto_20190419_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeinfo',
            name='hallPrice',
            field=models.IntegerField(default=1, verbose_name='会场参考价'),
            preserve_default=False,
        ),
    ]
