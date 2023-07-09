from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi
import os
from dotenv import load_dotenv
from numpy.random import randint


class StartController:
    def __init__(self):
        load_dotenv()

    @staticmethod
    def try_to_ping(mongo_client):
        try:
            mongo_client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            return mongo_client
        except Exception as e:
            print(e)

    def try_to_log_in(self, connection_string):
        mongo_client = MongoClient(connection_string, server_api=ServerApi('1'), tlsCAFile=certifi.where())

        return self.try_to_ping(mongo_client)

    def try_to_sign_up(self, user_name, password):
        mongo_client = MongoClient(os.getenv("SECRET_LINK_MONGO_ADMIN"), tlsCAFile=certifi.where())

        mongo_client.admin.command('createUser', user_name, pwd=password, roles=['readWrite'])

        return self.try_to_ping(mongo_client)

    def get_quote(self, connection_string):
        mongo_client = MongoClient(os.getenv("SECRET_LINK_MONGO_ADMIN"), tlsCAFile=certifi.where())

        random_quote_key = randint(1, 61)

        quote = mongo_client.quotes.start_quotes.find_one({str(random_quote_key): {"$exists": True}}, {"_id": 0})

        return quote[str(random_quote_key)]










