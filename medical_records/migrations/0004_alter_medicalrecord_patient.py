# Generated by Django 4.2 on 2024-03-08 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_remove_hospitalprofile_email_and_more'),
        ('medical_records', '0003_medicalrecord_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_records', to='profiles.patientprofile'),
        ),
    ]
