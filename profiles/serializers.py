from rest_framework import serializers
from accounts import models as acc_models
from . import models


class Location(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Location
        fields = ["url", "id", "name", "latitude", "longitude"]


class HospitalProfile(serializers.HyperlinkedModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        queryset=acc_models.CustomUser.objects.all()
    )
    location = serializers.PrimaryKeyRelatedField(
        queryset=models.Location.objects.all()
    )

    class Meta:
        model = models.HospitalProfile
        fields = [
            "url",
            "id",
            "owner",
            "name",
            "createdAt",
            "services",
            "email",
            "phone_number",
            "location",
        ]


class PatientProfile(serializers.HyperlinkedModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        queryset=acc_models.CustomUser.objects.all()
    )
    location = serializers.PrimaryKeyRelatedField(
        queryset=models.Location.objects.all()
    )

    class Meta:
        model = models.PatientProfile
        fields = [
            "url",
            "id",
            "owner",
            "date_of_birth",
            "createdAt",
            "phone_number",
            "location",
        ]


class HospitalService(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.HospitalService
        fields = [
            "url",
            "id",
            "name",
            "description",
            "category",
            "price",
            "availability",
        ]


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = models.Doctor
        fields = [
            "url",
            "user",
            "id",
            "name",
            "hospital",
        ]


class NurseSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = models.Nurse
        fields = [
            "url",
            "user",
            "id",
            "name",
            "hospital",
        ]
