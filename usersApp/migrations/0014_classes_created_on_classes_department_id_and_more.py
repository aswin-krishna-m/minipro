# Generated by Django 5.0.7 on 2024-09-19 09:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersApp', '0013_courses_short_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='created_on',
            field=models.DateField(default='2019-12-25'),
        ),
        migrations.AddField(
            model_name='classes',
            name='department_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='usersApp.department'),
        ),
        migrations.AddField(
            model_name='courses',
            name='created_on',
            field=models.DateField(default='2019-12-25'),
        ),
        migrations.AddField(
            model_name='department',
            name='created_on',
            field=models.DateField(default='2019-12-25'),
        ),
        migrations.AddField(
            model_name='student',
            name='created_on',
            field=models.DateField(default='2019-12-25'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='created_on',
            field=models.DateField(default='2019-12-25'),
        ),
    ]
