# Generated by Django 4.2 on 2023-05-08 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0010_alter_cursu_pr'),
    ]

    operations = [
        migrations.AddField(
            model_name='unemployed',
            name='rez',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
