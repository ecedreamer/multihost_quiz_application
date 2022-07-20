from django.test import TestCase, Client
from django.contrib.auth import get_user_model


User = get_user_model()


class TestLoginView(TestCase):
    def setUp(self) -> None:
        print("Starting")
        return super().setUp()

    def tearDown(self) -> None:
        print("Tearing down")
        return super().tearDown()

    def test_get_request(self):
        self.assertEqual(self.client.get("/api/v1/login").status_code, 405)

    def test_wrong_credentials(self):
        creds = {
            "email": "impossible@account.com",
            "password": "notrealpassword"
        }
        resp = self.client.post("/api/v1/login")
        self.assertEqual(resp.status_code, 401)

    def test_right_credentials(self):
        creds = {
            "email": "impossible@account.com",
            "password": "notrealpassword"
        }
        user = User.objects.create_user(**creds)
        self.assertNotEqual(user, None)
        resp = self.client.post("/api/v1/login", data=creds)
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(resp.get("secret"), None)