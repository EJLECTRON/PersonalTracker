from os import getenv
import certifi
from dotenv import load_dotenv
from pymongo.errors import OperationFailure, InvalidName
from ui_startInterface import *
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from numpy.random import randint

#for email, add to requirements
import smtplib
from random import randint
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




class StartModel:
    """ Custom class for start window"""

    def __init__(self, given_user_name = None, given_email = None, given_password = None, given_repeated_password = None, given_quote = None):
        load_dotenv()

        self.user_name = given_user_name
        self.password = given_password
        self.repeated_password = given_repeated_password
        self.quote = given_quote
        self.user_email = given_email
        self.pt_email = getenv("EMAIL")
        self.pt_email_password = getenv("PYCHARM_EMAIL_PASSWORD")
        self.smtp_server = getenv('SMTP_SERVER')
        self.smtp_port = getenv('SMTP_PORT')

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
        condition = self.user_name.strip() != "" and self.password.strip() != ""
        condition = condition and "$" not in self.user_name and "$" not in self.password
        condition = condition and self.user_name is not None and self.password is not None
        condition = condition and len(self.user_name) <= 30 and len(self.password) <= 30
        condition = condition and len(self.user_name) >= 3 and len(self.password) >= 3

        return condition
    def is_correct_data_for_sign_up(self):
        """ checks if given data to model is correct to sign up to db"""
        return self.is_correct_data_for_log_in() and self.password == self.repeated_password

    def try_to_log_in(self):
        connection_string = getenv("LINK_ADD_USER_PART1") + getenv("READ_ONLY_USER_LOGIN") + ":" + getenv("READ_ONLY_USER_PASSWORD") + getenv("LINK_ADD_USER_PART2")
        mongo_client = MongoClient(connection_string, server_api=ServerApi('1'), tlsCAFile=certifi.where())
        result = None

        try:
            password = mongo_client[getenv("USERS_DB_NAME")][self.user_name].find_one({"password": {'$exists': True}}, {"_id": 0})['password']
            if password == self.password:
                result = True

        except (OperationFailure, InvalidName, TypeError):
            pass

        return result

    def try_to_sign_up(self):
        mongo_client = MongoClient(getenv("SECRET_LINK_MONGO_ADMIN"), tlsCAFile=certifi.where())

        users_db = mongo_client[getenv("USERS_DB_NAME")]
        email_occupied = False
        for collection_name in users_db.list_collection_names():
            user_collection = users_db[collection_name]
            if user_collection.find_one({"email": self.user_email}):
                email_occupied = True
                break
        if self.user_name not in users_db.list_collection_names():
            if not email_occupied:
                try:
                    message = MIMEMultipart()
                    message['From'] = self.pt_email
                    message['To'] = self.user_email # This is the recipient's email address
                    code = ""
                    for _ in range(4):
                        digit = randint(0, 9)
                        code += str(digit)
                    message['Subject'] = "Personal Tracker Registration"
                    body = "Hello! Someone is trying to register an account at the Personal Tracker app using your e-mail address. Unless you were mistaken, enter this code {}".format(code)
                    message.attach(MIMEText(body, 'plain'))
                    server = smtplib.SMTP(self.smtp_server, self.smtp_port)
                    server.starttls()
                    server.login(self.pt_email, self.pt_email_password)
                    server.sendmail(self.pt_email, self.user_email, message.as_string())
                    server.quit()
                    return code
                except:
                    return 3
            else:
                return 5
        else:
            return 2

    def add_new_user(self):
        mongo_client = MongoClient(getenv("SECRET_LINK_MONGO_ADMIN"), tlsCAFile=certifi.where())
        users_db = mongo_client[getenv("USERS_DB_NAME")]
        users_db.create_collection(self.user_name)
        users_db[self.user_name].insert_one({"password": self.password, "email": self.user_email})





    @staticmethod
    def get_quote():
        connection_string = getenv("SECRET_LINK_MONGO_ADMIN")
        mongo_client = MongoClient(connection_string, tlsCAFile=certifi.where())
        random_quote_key = randint(1, 61)
        quote = mongo_client.quotes.start_quotes.find_one({str(random_quote_key): {"$exists": True}}, {"_id": 0})
        return quote[str(random_quote_key)]

