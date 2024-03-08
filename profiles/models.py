from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from accounts import models as acc_models


class Profile(models.Model):
    user = models.OneToOneField(
        "accounts.CustomUser",
        verbose_name=_("User Account"),
        related_name="profile",
        on_delete=models.CASCADE,
    )
    hospital_profile = models.ForeignKey(
        "profiles.HospitalProfile",
        verbose_name=_("Hospital profile"),
        related_name="profile_hospital",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    patient_profile = models.OneToOneField(
        "profiles.PatientProfile",
        verbose_name=_("Patient profile"),
        related_name="profile_patient",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class HospitalProfile(models.Model):
    name = models.CharField(_("Hospital Name"), max_length=50)
    createdAt = models.DateTimeField(
        _("Date the hospital was added "), auto_now_add=True
    )
    updatedAt = models.DateTimeField(
        _("Date the hospital details were updated "), auto_now=True
    )
    phone_number = PhoneNumberField(
        region="KE",
        blank=True,
        null=True,
    )
    location = models.ForeignKey(
        "profiles.Location",
        verbose_name=_("Location of the hospital"),
        related_name="hospital",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name} - {self.location}"


class PatientProfile(models.Model):
    user = models.OneToOneField(
        "accounts.CustomUser",
        verbose_name=_("User Account"),
        related_name="patient_account_profile",
        on_delete=models.CASCADE,
    )
    date_of_birth = models.DateField(
        _("Date of Birth"),
        blank=True,
        null=True,
    )
    phone_number = PhoneNumberField(
        region="KE",
        blank=True,
        null=True,
    )
    location = models.ForeignKey(
        "profiles.Location",
        verbose_name=_("Location of the patient"),
        related_name="patient",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    createdAt = models.DateTimeField(
        _("Date the patient was added "), auto_now_add=True
    )
    updatedAt = models.DateTimeField(
        _("Date the patient details were updated "), auto_now=True
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class HospitalService(models.Model):
    CATEGORY_CHOICES = [
        ("diagnostic", "Diagnostic"),
        ("surgical", "Surgical"),
        ("therapeutic", "Therapeutic"),
        ("preventive", "Preventive"),
        ("emergency", "Emergency"),
        ("maternity", "Maternity"),
        ("rehabilitation", "Rehabilitation"),
    ]

    description = models.TextField(
        blank=True,
        null=True,
    )
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.category


class Location(models.Model):
    address = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.address


class Doctor(models.Model):
    name = models.OneToOneField(acc_models.CustomUser, on_delete=models.CASCADE)
    hospital = models.ForeignKey(HospitalProfile, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(_("Date the doctor was added "), auto_now_add=True)
    updatedAt = models.DateTimeField(
        _("Date the doctor details were updated "), auto_now=True
    )

    def __str__(self):
        return f"{self.name.first_name} {self.name.last_name}"


class Nurse(models.Model):
    name = models.OneToOneField(acc_models.CustomUser, on_delete=models.CASCADE)
    hospital = models.ForeignKey(HospitalProfile, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(_("Date the nurse was added "), auto_now_add=True)
    updatedAt = models.DateTimeField(
        _("Date the nurse details were updated "), auto_now=True
    )

    def __str__(self):
        return f"{self.name.first_name} {self.name.last_name}"
