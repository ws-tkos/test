# Generated by Django 3.0.4 on 2020-04-03 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_coursesignin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursesignin',
            name='signIn_bool',
        ),
    ]
