from django.db import models
from profiles import models as prof_models
from django.utils.translation import gettext_lazy as _

class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        prof_models.PatientProfile, on_delete=models.CASCADE, related_name="medical_records"
    )
    hospital = models.ForeignKey(
        "profiles.HospitalProfile", on_delete=models.SET_NULL, null=True, blank=True
    )
    name = models.CharField(_("Medical Record Name"), max_length=50)
    symptoms = models.TextField()
    diagnosis = models.TextField()
    prescribed_medications = models.TextField()
    notes = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Medical Record for {self.patient.first_name} {self.patient.first_name} - {self.created_at} at {self.hospital}"
