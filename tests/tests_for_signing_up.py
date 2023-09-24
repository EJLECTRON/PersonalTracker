import unittest
from os import getenv
from dotenv import load_dotenv
from start_model import StartModel
import random
import string


class TestRegistration(unittest.TestCase):

    @staticmethod
    def generate_random_string():
        min_length = 3
        max_length = 30

        characters = string.ascii_letters + string.digits + string.punctuation + " " + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' + "ґєії"
        length = random.randint(min_length, max_length)

        random_string = ''.join(random.choice(characters) for _ in range(length))

        return random_string

    def setUp(self):
        self.start_model = StartModel()
        load_dotenv()

    def test_existing_username(self):
        self.start_model.user_name = getenv("TEST_USERNAME2")
        self.start_model.password = "1234"
        self.start_model.repeated_password = "1234"
        self.start_model.user_email = getenv("TEST_EMAIL1")
        result = self.start_model.try_to_sign_up()
        self.assertEqual(result, 2)

    def test_existing_email(self):
        self.start_model.user_name = "testuser"
        self.start_model.password = "password123"
        self.start_model.repeated_password = "password123"
        self.start_model.user_email = getenv("TEST_EMAIL2")
        result = self.start_model.try_to_sign_up()
        self.assertEqual(result, 5)

    def test_valid_registration(self):
        for i in range (20):
            self.start_model.user_name = self.generate_random_string()
            self.start_model.password = self.generate_random_string()
            self.start_model.repeated_password = self.start_model.password
            self.start_model.user_email = getenv("TEST_EMAIL1")
            result = self.start_model.try_to_sign_up()
            print(f"username:{self.start_model.user_name}, password:{self.start_model.password}, mail:{self.start_model.user_email}")
            self.assertTrue(result.isdigit() and len(result) == 4)

    def test_wrong_email_format(self):
        self.start_model.user_name = "testuser"
        self.start_model.password = "123"
        self.start_model.repeated_password = "123"
        self.start_model.user_email = "email"
        result = self.start_model.try_to_sign_up()
        self.assertEqual(result, 3)



if __name__ == '__main__':
    unittest.main()
