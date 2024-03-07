# Generated by Django 4.2 on 2024-03-07 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Hospital Name')),
                ('createdAt', models.DateTimeField(auto_now=True, verbose_name='Date the hospital details were updated ')),
                ('email', models.EmailField(max_length=254, verbose_name='Email address')),
                ('phone_number', models.CharField(max_length=10, verbose_name='Phone Number')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('phone_number', models.CharField(max_length=10, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email address')),
                ('createdAt', models.DateTimeField(auto_now=True, verbose_name='Date the patient details were updated ')),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='profiles.location', verbose_name='Location of the patient')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('diagnostic', 'Diagnostic'), ('surgical', 'Surgical'), ('therapeutic', 'Therapeutic'), ('preventive', 'Preventive'), ('emergency', 'Emergency'), ('maternity', 'Maternity'), ('rehabilitation', 'Rehabilitation')], max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('availability', models.BooleanField(default=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospital_service', to='profiles.hospitalprofile', verbose_name='Service offered')),
            ],
        ),
        migrations.AddField(
            model_name='hospitalprofile',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hospital', to='profiles.location', verbose_name='Location of the hospital'),
        ),
    ]
