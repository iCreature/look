# Generated by Django 3.1 on 2020-11-09 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_test_info_course_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_info',
            name='type',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
