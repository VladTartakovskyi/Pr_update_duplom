# Generated by Django 4.1.2 on 2022-11-05 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profession',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='vacancies',
            name='slug',
        ),
    ]
