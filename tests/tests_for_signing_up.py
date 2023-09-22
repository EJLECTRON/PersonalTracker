import unittest
from os import getenv
from dotenv import load_dotenv
from start_model import StartModel


class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.start_model = StartModel()
        load_dotenv()

    def test_valid_registration(self):
        self.start_model.user_name = "hello"
        self.start_model.password = "kitty"
        self.start_model.repeated_password = "kitty"
        self.start_model.user_email = getenv("TEST_EMAIL1")
        result = self.start_model.try_to_sign_up()
        self.assertTrue(result.isdigit() and len(result) == 4)

    def test_existing_username(self):
        self.start_model.user_name = getenv("TEST_USERNAME2")
        self.start_model.password = "1234"
        self.start_model.repeated_password = "1234"
        self.start_model.user_email = getenv("TEST_EMAIL2")
        result = self.start_model.try_to_sign_up()
        self.assertEqual(result, 2)

    def test_existing_email(self):
        self.start_model.user_name = "testuser"
        self.start_model.password = "password123"
        self.start_model.repeated_password = "password123"
        self.start_model.user_email = getenv("TEST_EMAIL2")
        result = self.start_model.try_to_sign_up()
        self.assertEqual(result, 5)

    def test_wrong_email_format(self):
        self.start_model.user_name = "testuser"
        self.start_model.password = "password123"
        self.start_model.repeated_password = "password456"
        self.start_model.user_email = "email"
        result = self.start_model.try_to_sign_up()
        self.assertEqual(result, 3)



if __name__ == '__main__':
    unittest.main()
