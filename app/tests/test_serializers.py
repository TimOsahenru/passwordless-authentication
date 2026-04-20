from django.test import TestCase
from app.serializers import LoginSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginSerializerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="adminuser", email="admin@gmail.com", password="12345")



    def test_serializer_validates_email_login(self):
        data = {
            "email": "admin@gmail.com",
            "password": "12345",
        }
        serializer = LoginSerializer(data=data)

        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["user"], self.user)



    def test_serializer_fails_with_invalid_creds(self):
        data = {
            "email": "admin@gmail.com",
            "password": "12346"
        }

        serializer = LoginSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("non_field_errors", serializer.errors)
        self.assertEqual(serializer.errors["non_field_errors"][0], "Invalid credentials")