from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from accounts import models as acc_models


class Profile(models.Model):
    user = models.OneToOneField("accounts.CustomUser", verbose_name=_("User profile"), related_name="profile",on_delete=models.CASCADE)
    hospital_profile = models.ForeignKey("profiles.HospitalProfile", verbose_name=_("Hospital profile"), on_delete=models.CASCADE)
    hospital_profile = models.OneToOneField("profiles.PatientProfile", verbose_name=_("Patient profile"), on_delete=models.CASCADE)

class HospitalProfile(models.Model):
    owner = models.ForeignKey(
        "accounts.CustomUser",
        verbose_name=_("Hospital Owner"),
        related_name="hospital",
        on_delete=models.CASCADE,
    )
    name = models.CharField(_("Hospital Name"), max_length=50)
    createdAt = models.DateTimeField(
        _("Date the hospital was added "), auto_now_add=True
    )
    updatedAt = models.DateTimeField(
        _("Date the hospital details were updated "), auto_now=True
    )
    email = models.EmailField(_("Email address"), max_length=254)
    phone_number = PhoneNumberField(region="KE")
    location = models.ForeignKey(
        "profiles.Location",
        verbose_name=_("Location of the hospital"),
        related_name="hospital",
        on_delete=models.CASCADE,
    )
    services = models.ForeignKey(
        "profiles.HospitalService",
        verbose_name=_("Services offered"),
        related_name="hospital",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.name} - {self.location}"


class PatientProfile(models.Model):
    owner = models.OneToOneField(
        "accounts.CustomUser",
        verbose_name=_("Patient Owner"),
        related_name="patient",
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    date_of_birth = models.DateField(_("Date of Birth"))
    phone_number = PhoneNumberField(region="KE")
    email = models.EmailField(_("Email address"), max_length=254)
    location = models.ForeignKey(
        "profiles.Location",
        verbose_name=_("Location of the patient"),
        related_name="patient",
        on_delete=models.CASCADE,
    )
    createdAt = models.DateTimeField(
        _("Date the patient was added "), auto_now_add=True
    )
    updatedAt = models.DateTimeField(
        _("Date the patient details were updated "), auto_now=True
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


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

    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.ForeignKey(acc_models.CustomUser, on_delete=models.CASCADE)
    hospital = models.ForeignKey(HospitalProfile, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(_("Date the doctor was added "), auto_now_add=True)
    updatedAt = models.DateTimeField(
        _("Date the doctor details were updated "), auto_now=True
    )

    def __str__(self):
        return f"{self.name.first_name} {self.name.last_name}"


class Nurse(models.Model):
    name = models.ForeignKey(acc_models.CustomUser, on_delete=models.CASCADE)
    hospital = models.ForeignKey(HospitalProfile, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(_("Date the nurse was added "), auto_now_add=True)
    updatedAt = models.DateTimeField(
        _("Date the nurse details were updated "), auto_now=True
    )

    def __str__(self):
        return f"{self.name.first_name} {self.name.last_name}"
