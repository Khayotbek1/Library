# Generated by Django 5.1.6 on 2025-03-08 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_libraryadmin_working_hours_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='libraryadmin',
            name='working_hours',
            field=models.TimeField(null=True),
        ),
    ]
