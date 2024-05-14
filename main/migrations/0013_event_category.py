# Generated by Django 5.0.3 on 2024-05-14 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_event_attendee_responses_event_attendees_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.CharField(blank=True, choices=[('work', 'Work'), ('personal', 'Personal'), ('social', 'Social'), ('holiday', 'Holiday')], max_length=20, null=True),
        ),
    ]
