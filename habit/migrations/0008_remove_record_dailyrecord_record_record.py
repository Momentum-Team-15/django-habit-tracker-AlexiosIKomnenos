# Generated by Django 4.1.3 on 2022-11-07 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0007_record_dailyrecord'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='record',
            name='dailyrecord',
        ),
        migrations.AddConstraint(
            model_name='record',
            constraint=models.UniqueConstraint(fields=('habitrecord', 'date'), name='record'),
        ),
    ]
