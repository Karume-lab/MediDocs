from rest_framework import serializers
from accounts import models as acc_models
from . import models


class Profile(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Profile
        fields = "__all__"
        extra_kwargs = {
            "url": {"view_name": "profile-detail", "lookup_field": "pk"},
            "user": {"view_name": "customuser-detail", "lookup_field": "pk"},
            "hospital_profile": {
                "view_name": "hospitalprofile-detail",
                "lookup_field": "pk",
            },
            "patient_profile": {
                "view_name": "patientprofile-detail",
                "lookup_field": "pk",
            },
        }


class HospitalProfile(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.HospitalProfile
        fields = "__all__"
        extra_kwargs = {
            "url": {"view_name": "hospitalprofile-detail", "lookup_field": "pk"},
            "location": {"view_name": "location-detail", "lookup_field": "pk"},
            "services": {"view_name": "hospitalservice-detail", "lookup_field": "pk"},
        }


class Location(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Location
        fields = ["url", "id", "address", "latitude", "longitude"]


class PatientProfile(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PatientProfile
        fields = "__all__"
        extra_kwargs = {
            "url": {"view_name": "patientprofile-detail", "lookup_field": "pk"},
            "location": {"view_name": "location-detail", "lookup_field": "pk"},
        }


class HospitalService(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.HospitalService
        fields = [
            "url",
            "id",
            "description",
            "category",
            "availability",
        ]


class Doctor(serializers.HyperlinkedModelSerializer):
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


class Nurse(serializers.HyperlinkedModelSerializer):
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
