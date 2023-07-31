from os import getenv
import certifi
from dotenv import load_dotenv
from ui_startInterface import *
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from numpy.random import randint


class StartModel(QtWidgets.QWidget):
    """ Custom class for start window"""

    def __init__(self, user_name = None, password = None, repeated_password = None, quote = None):
        load_dotenv()

        super().__init__()
        self._user_name = user_name
        self._password = password
        self._repeated_password = repeated_password
        self._quote = quote

    def is_correct_data_for_log_in(self):
        """ checks if given data to model is correct to log in to db"""
        return self._user_name is not None and self._password is not None and self._user_name != "" and self._password != ""

    def is_correct_data_for_sign_up(self):
        """ checks if given data to model is correct to sign up to db"""
        return self.is_correct_data_for_log_in() and self._password == self._repeated_password

    def try_to_log_in(self):
        connection_string = getenv("LINK_ADD_USER_PART1") + self._user_name + ":" + self._password + getenv("LINK_ADD_USER_PART2")
        mongo_client = MongoClient(connection_string, server_api=ServerApi('1'), tlsCAFile=certifi.where())

    def try_to_sign_up(self):
        #db = getenv("LINK_ADD_USER_PART1") + self._user_name + ":" + self._password + getenv("LINK_ADD_USER_PART2")
        mongo_client = MongoClient(getenv("SECRET_LINK_MONGO_ADMIN"), tlsCAFile=certifi.where())
        mongo_client.admin.command('createUser', self._user_name, pwd=self._password, roles=['readWrite'])
        result = self._password.try_to_sign_up(self._user_name, self._password)

    def get_quote(self):
        connection_string = getenv("SECRET_LINK_MONGO_ADMIN")
        mongo_client = MongoClient(connection_string, tlsCAFile=certifi.where())
        random_quote_key = randint(1, 61)
        quote = mongo_client.quotes.start_quotes.find_one({str(random_quote_key): {"$exists": True}}, {"_id": 0})
        return quote[str(random_quote_key)]


    """
    def create_main_window(self):
        temp_client = User(self.username, self._password)
        main_window = MainWindow(temp_client)
        main_window.show()
    """






