# Generated by Django 3.0.4 on 2020-03-31 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20200331_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='student',
        ),
        migrations.RemoveField(
            model_name='course',
            name='teacher',
        ),
    ]