# Generated by Django 3.2.8 on 2021-11-26 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GTEAMS_APP', '0005_practice_title_tui'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practice_title',
            name='tui',
        ),
    ]
