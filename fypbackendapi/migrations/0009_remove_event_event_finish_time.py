# Generated by Django 3.2.6 on 2021-10-10 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fypbackendapi', '0008_alter_event_event_finish_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_Finish_Time',
        ),
    ]