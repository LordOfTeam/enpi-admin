# Generated by Django 2.1.7 on 2019-04-16 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20190414_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeinfo',
            name='maxAllPeople',
            field=models.IntegerField(default=2, help_text='整数', verbose_name='最多可容纳人数'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='placeinfo',
            name='maxBallroomArea',
            field=models.IntegerField(default=2, help_text='整数', verbose_name='最大宴会厅面积'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='placeinfo',
            name='roomNum',
            field=models.IntegerField(default=2, help_text='整数', verbose_name='会场数量'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='placeinfo',
            name='rooms',
            field=models.ManyToManyField(related_name='rooms', to='backend.GuestRoom', verbose_name='客房'),
        ),
    ]
