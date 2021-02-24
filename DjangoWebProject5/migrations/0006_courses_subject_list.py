# Generated by Django 3.1 on 2020-10-29 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201029_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=255)),
                ('course_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='subject_list',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_id', models.CharField(max_length=255)),
                ('module', models.CharField(max_length=255)),
            ],
        ),
    ]