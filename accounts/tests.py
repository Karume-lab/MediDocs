from django.contrib.auth import get_user_model
from django.test import TestCase
from . import serializers as acc_serializers

User = get_user_model()


class UserSerializerTestCase(TestCase):
    """
    Test case for the UserSerializer class.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.validated_data = {
            "email": "test@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "username": "johndoe",
            "password": "testpassword",
        }

    def test_create_user(self):
        """
        Test the create method of UserSerializer.
        """
        serializer = acc_serializers.UserSerializer(data=self.validated_data)
        self.assertTrue(serializer.is_valid())

        user = serializer.save()
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, self.validated_data["email"])
        self.assertEqual(user.first_name, self.validated_data["first_name"])
        self.assertEqual(user.last_name, self.validated_data["last_name"])
        self.assertEqual(user.username, self.validated_data["username"])

        # Verify that the password is correctly set and hashed
        self.assertTrue(user.check_password(self.validated_data["password"]))

    def test_create_user_invalid_data(self):
        """
        Test the create method of UserSerializer with invalid data.
        """
        # Test with missing required fields
        invalid_data = {
            "email": "test@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "username": "johndoe",
        }
        serializer = acc_serializers.UserSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)

        # Test with an existing username
        existing_user = User.objects.create_user(**self.validated_data)
        duplicate_username_data = {
            "email": "another@example.com",
            "first_name": "Jane",
            "last_name": "Smith",
            "username": self.validated_data["username"],
            "password": "test123",
        }
        serializer = acc_serializers.UserSerializer(data=duplicate_username_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("username", serializer.errors)


from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status
from .views import UserViewSet


class UserViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.viewset = UserViewSet.as_view({"get": "list", "post": "create"})
        self.valid_payload = {
            "email": "test@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "username": "johndoe",
            "password": "testpassword",
        }
        self.invalid_payload = {
            "email": "test@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "username": "johndoe",
        }

    def test_list_users(self):
        request = self.factory.get("/users/")
        response = self.viewset(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        request = self.factory.post("/users/", self.valid_payload)
        response = self.viewset(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().email, self.valid_payload["email"])

    def test_create_user_invalid_data(self):
        request = self.factory.post("/users/", self.invalid_payload)
        response = self.viewset(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)
