from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")

    def test_login(self):
        login = self.client.login(username="testuser", password="password123")
        self.assertTrue(login)
