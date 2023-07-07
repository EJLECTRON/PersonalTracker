from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi
import os
from dotenv import load_dotenv


class StartController:
    def __init__(self):
        load_dotenv()

    def try_to_log_in(self, db):
        mongo_client = MongoClient(db, server_api=ServerApi('1'), tlsCAFile=certifi.where())

        return self.try_to_ping(mongo_client)

    def try_to_sign_up(self, user_name, password):
        mongo_client = MongoClient(os.getenv("SECRET_LINK_MONGO_ADMIN"), tlsCAFile=certifi.where())

        mongo_client.admin.command('createUser', user_name, pwd=password, roles=['readWrite'])

        return self.try_to_ping(mongo_client)

    @staticmethod
    def try_to_ping(mongo_client):
        try:
            mongo_client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            return mongo_client
        except Exception as e:
            print(e)










