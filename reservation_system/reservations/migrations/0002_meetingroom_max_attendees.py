# Generated by Django 4.2.6 on 2024-09-10 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetingroom',
            name='max_attendees',
            field=models.IntegerField(default=5),
        ),
    ]
