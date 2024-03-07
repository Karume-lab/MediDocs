from rest_framework import viewsets
from . import models
from . import serializers


class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = models.MedicalRecord.objects.all()
    serializer_class = serializers.MedicalRecordSerializer
