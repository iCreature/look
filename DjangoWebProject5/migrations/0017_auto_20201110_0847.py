# Generated by Django 3.1 on 2020-11-10 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20201110_0743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submitted',
            name='exam_id',
        ),
        migrations.AlterField(
            model_name='submitted',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='submitted',
            name='time',
            field=models.TimeField(auto_now=True, null=True),
        ),
    ]
