# Generated by Django 3.2.8 on 2021-11-26 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GTEAMS_APP', '0004_rename_subject_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='practice_title',
            name='tui',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
