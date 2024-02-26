import unittest

from authentication.login import login

class TestLogin(unittest.TestCase):
    def test_login_without_body(self):
        data = dict({})
        response = login(data, None)
        self.assertEqual(response["statusCode"], 400)

    def test_login_without_username(self):
        data = {"body": {"password": "abcdeA@123"}}
        response = login(data, None)
        self.assertEqual(response["statusCode"], 400)

    def test_login_without_password(self):
        data = {"body": {"username": "devsid2023"}}
        response = login(data, None)
        self.assertEqual(response["statusCode"], 400)

    def test_login_with_invalid_username(self):
        data = {"body": {"username": "abcdef", "password": "abcdeA@123"}}
        response = login(data, None)
        self.assertEqual(response["statusCode"], 400)

    def test_login_with_invalid_password(self):
        data = {"body": {"username": "devsid2023", "password": "abcdef"}}
        response = login(data, None)
        self.assertEqual(response["statusCode"], 400)

    def test_login_with_valid_credentials(self):
        data = {"body": {"username": "devsid2023", "password": "abcdeA@123"}}
        response = login(data, None)
        self.assertEqual(response["statusCode"], 200)
