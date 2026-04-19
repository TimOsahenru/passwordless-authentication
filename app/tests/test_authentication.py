from django.test import TestCase
from django.contrib.auth import get_user_model
from app.authentication import EmailAuthBackend


User = get_user_model()


class EmailBackendTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="adminuser", email="admin@gmail.com", password="12345")
        self.backend = EmailAuthBackend()



    def test_auth_success(self):
        user = self.backend.authenticate(None, username="admin@gmail.com", password="12345")
        self.assertEqual(user, self.user)


    def auth_fail_wrong_password(self):
        user = self.backend.authenticate(None, username="admin@gmail.com", password="12345")
        self.assertIsNone(user)