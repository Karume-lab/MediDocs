from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import MedicalRecord
from profiles import models

User = get_user_model()


class PatientProfileModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword",
        )
        self.location = models.Location.objects.create(
            name="Test Location",
            address="Testing",
            latitude=123.456,
            longitude=789.012,
        )
        self.patient_profile = models.PatientProfile.objects.create(
            owner=self.user,
            first_name="John",
            last_name="Doe",
            date_of_birth="2000-01-01",
            phone_number="+254712345678",
            email="john.doe@example.com",
            location=self.location,
        )

    def test_patient_profile_str(self):
        expected_str = (
            f"{self.patient_profile.first_name} {self.patient_profile.last_name}"
        )
        self.assertEqual(str(self.patient_profile), expected_str)


class LocationModelTestCase(TestCase):
    def setUp(self):
        self.location = models.Location.objects.create(
            name="Test Location",
            address="Testing",
            latitude=123.456,
            longitude=789.012,
        )

    def test_location_str(self):
        expected_str = "Test Location"
        self.assertEqual(str(self.location), expected_str)


class HospitalServiceModelTestCase(TestCase):
    def setUp(self):
        self.hospital_service = models.HospitalService.objects.create(
            name="Test Service",
            description="Test service description",
            category="diagnostic",
            price=100.00,
            availability=True,
        )

    def test_hospital_service_str(self):
        expected_str = "Test Service"
        self.assertEqual(str(self.hospital_service), expected_str)
