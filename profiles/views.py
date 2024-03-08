from rest_framework import viewsets
from . import models
from . import serializers
from . import permissions
from medical_records import serializers as med_serializers, models as med_models


class HospitalProfileViewSet(viewsets.ModelViewSet):
    queryset = models.HospitalProfile.objects.all().order_by("id")
    serializer_class = serializers.HospitalProfile

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PatientProfileViewSet(viewsets.ModelViewSet):
    queryset = models.PatientProfile.objects.all().order_by("id")
    serializer_class = serializers.PatientProfile


class LocationViewSet(viewsets.ModelViewSet):
    queryset = models.Location.objects.all().order_by("id")
    serializer_class = serializers.Location


class HospitalServiceViewSet(viewsets.ModelViewSet):
    queryset = models.HospitalService.objects.all().order_by("id")
    serializer_class = serializers.HospitalService


class MedicalRecordViewSet(viewsets.ModelViewSet):
    serializer_class = med_serializers.MedicalRecordSerializer
    queryset = med_models.MedicalRecord.objects.all().order_by("id")
    permission_classes = [permissions.DoctorPermission]


class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DoctorSerializer
    queryset = models.Doctor.objects.all().order_by("id")
    permission_classes = [permissions.DoctorPermission]


class NurseViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.NurseSerializer
    queryset = models.Nurse.objects.all().order_by("id")
    permission_classes = [permissions.NursePermission]
