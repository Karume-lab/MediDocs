from django.db import models
from django.contrib.auth import get_user_model


class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="medical_records"
    )
    hospital = models.ForeignKey(
        "profiles.HospitalProfile", on_delete=models.SET_NULL, null=True, blank=True
    )
    symptoms = models.TextField()
    diagnosis = models.TextField()
    prescribed_medications = models.TextField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Medical Record for {self.patient.first_name} {self.patient.first_name} - {self.created_at} at {self.hospital}"
