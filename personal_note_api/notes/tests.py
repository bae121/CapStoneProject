from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="password123"
        )

    def test_user_creation(self):
        """Ensure the user is created with the correct username"""
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertTrue(self.user.check_password("password123"))

    def test_login(self):
        """Ensure the test client can log in with correct credentials"""
        login_successful = self.client.login(username="testuser", password="password123")
        self.assertTrue(login_successful)

    def test_login_with_wrong_password(self):
        """Ensure login fails with incorrect credentials"""
        login_failed = self.client.login(username="testuser", password="wrongpassword")
        self.assertFalse(login_failed)
