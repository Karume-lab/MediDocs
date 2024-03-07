from django.test import TestCase
from accounts.models import CustomUser
from . import models
from . import serializers


class LocationSerializerTestCase(TestCase):
    def setUp(self):
        self.location_data = {
            "name": "Test Location",
            "latitude": 123.456,
            "longitude": 789.012,
        }

    def test_location_serializer(self):
        serializer = serializers.Location(data=self.location_data)
        self.assertTrue(serializer.is_valid())

        location = serializer.save()
        self.assertIsInstance(location, models.Location)
        self.assertEqual(location.name, self.location_data["name"])
        self.assertNotEqual(location.latitude, self.location_data["latitude"])
        self.assertNotEqual(location.longitude, self.location_data["longitude"])
