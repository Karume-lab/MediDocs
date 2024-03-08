# Generated by Django 4.2 on 2024-03-08 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_records', '0002_medicalrecord_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalrecord',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='Medical Record Name'),
            preserve_default=False,
        ),
    ]