# Generated by Django 2.2.12 on 2020-06-03 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AWSD', '0002_auto_20200603_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membersmodel',
            name='Members_periods',
            field=models.ManyToManyField(to='AWSD.ActivityModel'),
        ),
    ]
