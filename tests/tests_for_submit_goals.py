import unittest
from user_class import User
from start_model import StartModel
import random
import string


class TestLogIn(unittest.TestCase):
    user = User('login', 'F5YMtBhoIdLuHjog')

    @staticmethod
    def generate_random_string():
        min_length = 3
        max_length = 30

        characters = string.ascii_letters + string.digits + string.punctuation + " " + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' + "ґєії"
        length = random.randint(min_length, max_length)

        random_string = ''.join(random.choice(characters) for _ in range(length))

        return random_string
    def test_try_to_log_in_1(self):
        model = StartModel("login", None, "F5YMtBhoIdLuHjog")
        if model.is_correct_data_for_log_in():
            self.assertEqual(model.try_to_log_in(), True)

    def test_try_to_log_in_2(self):
        model = StartModel("sasha", None, "1234")
        if model.is_correct_data_for_log_in():
            self.assertEqual(model.try_to_log_in(), True)

    def test_try_to_log_in_3(self):
        model = StartModel("qwe", None, "qwe")
        if model.is_correct_data_for_log_in():
            self.assertEqual(model.try_to_log_in(), True)

    def test_try_to_log_in_4(self):
        model = StartModel("the", None, "123")
        if model.is_correct_data_for_log_in():
            self.assertEqual(model.try_to_log_in(), True)

    def test_try_to_log_in_5(self):
        for _ in range(1800):
            model = StartModel(TestLogIn().generate_random_string(), None, TestLogIn().generate_random_string())
            if model.is_correct_data_for_log_in():
                self.assertEqual(model.try_to_log_in(), None)
            print(f"{_} passed, username:{model.user_name}, password:{model.password}")
    def test_try_to_log_in_6(self):
        model = StartModel(".пBg9Xіrp\\nл.ч", None, "123")
        if model.is_correct_data_for_log_in():
            self.assertEqual(model.try_to_log_in(), None)


if __name__ == '__main__':
    unittest.main()