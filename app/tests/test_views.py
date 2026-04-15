from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class LoginAPIViewTestCase(APITestCase):
    def setUp(self):
        self.username = "admin"
        self.email = "admin@gmail.com"
        self.password = "password1234"

        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            email=self.email,
        )

        self.url = reverse("login_user")



    def test_login_success(self):
        """Test that a user can login with valid credentials"""
        data = {
            "username": self.username,
            "password": self.password,
        }

        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Login successful")
        self.assertEqual(response.data["user"]["username"], self.username)


    def test_login_invalid_credentials(self):
        """Test that the login fails with a wrong password"""
        data = {
            "username": self.username,
            "password": "123555",
        }
        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn("user", response.data)


    def test_login_missing_field(self):
        """Test that login fails if field are missing."""
        data = {"username": self.username}
        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)