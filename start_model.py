from os import getenv
import certifi
from dotenv import load_dotenv
from ui_startInterface import *
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from numpy.random import randint


class StartModel(QtWidgets.QWidget):
    """ Custom class for start window"""

    def __init__(self, given_user_name = None, given_password = None, given_repeated_password = None, given_quote = None):
        load_dotenv()   

        super().__init__()
        self.user_name = given_user_name
        self.password = given_password
        self.repeated_password = given_repeated_password
        self.quote = given_quote

    @property
    def user_name(self):
        return self._user_name
    @user_name.setter
    def user_name(self, given_user_name):
        self._user_name = given_user_name

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, given_password):
        self._password = given_password

    @property
    def repeated_password(self):
        return self._repeated_password

    @repeated_password.setter
    def repeated_password(self, given_repeated_password):
        self._repeated_password = given_repeated_password

    @property
    def quote(self):
        return self._quote

    @quote.setter
    def quote(self, given_quote):
        self._quote = given_quote


    def is_correct_data_for_log_in(self):
        """ checks if given data to model is correct to log in to db"""
        return self.user_name is not None and self.password is not None and self.user_name != "" and self.password != ""

    def is_correct_data_for_sign_up(self):
        """ checks if given data to model is correct to sign up to db"""
        return self.is_correct_data_for_log_in() and self.password == self.repeated_password

    def try_to_log_in(self):
        connection_string = getenv("LINK_ADD_USER_PART1") + self.user_name + ":" + self.password + getenv("LINK_ADD_USER_PART2")
        mongo_client = MongoClient(connection_string, server_api=ServerApi('1'), tlsCAFile=certifi.where())

    def try_to_sign_up(self):
        #db = getenv("LINK_ADD_USER_PART1") + user_name + ":" + password + getenv("LINK_ADD_USER_PART2")
        mongo_client = MongoClient(getenv("SECRET_LINK_MONGO_ADMIN"), tlsCAFile=certifi.where())
        mongo_client.admin.command('createUser', self.user_name, pwd=self.password, roles=['readWrite'])
        result = self.password.try_to_sign_up(self.user_name, self.password)

    @staticmethod
    def get_quote():
        connection_string = getenv("SECRET_LINK_MONGO_ADMIN")
        mongo_client = MongoClient(connection_string, tlsCAFile=certifi.where())
        random_quote_key = randint(1, 61)
        quote = mongo_client.quotes.start_quotes.find_one({str(random_quote_key): {"$exists": True}}, {"_id": 0})
        return quote[str(random_quote_key)]


    """
    def create_main_window(self):
        temp_client = User(username, password)
        main_window = MainWindow(temp_client)
        main_window.show()
    """






