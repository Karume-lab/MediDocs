# Generated by Django 4.2 on 2024-03-07 14:09

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_hospitalprofile_owner_patientprofile_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitalprofile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]