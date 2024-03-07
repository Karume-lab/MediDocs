from rest_framework import viewsets
from . import models
from . import serializers


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
