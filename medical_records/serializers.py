from rest_framework import serializers
from .models import MedicalRecord


class MedicalRecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = (
            "patient",
            "hospital",
            "name",
            "diagnosis",
            "symptoms",
            "prescribed_medications",
            "notes",
        )
        extra_kwargs = {
            "url": {"view_name": "medicalrecord-detail"},
            "patient": {"view_name": "patientprofile-detail"},
            "hospital": {"view_name": "hospitalprofile-detail"},
        }
