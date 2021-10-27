# Generated by Django 3.2.6 on 2021-10-25 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fypbackendapi', '0011_alter_event_event_finish_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipper_name', models.CharField(max_length=150)),
                ('shipper_email', models.EmailField(max_length=100)),
                ('shipper_image', models.ImageField(upload_to='uploads/images')),
                ('shipper_phone_no', models.CharField(max_length=20)),
                ('shipper_address', models.CharField(max_length=200)),
                ('shipper_Regiter_Date', models.DateField()),
                ('shipper_verified', models.BooleanField()),
            ],
        ),
    ]
