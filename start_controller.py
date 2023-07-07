from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi
import os
from dotenv import load_dotenv
class StartController:
    def __init__(self):
        load_dotenv()
        pass

    def try_to_log_in(self, db):
        mongo_client = MongoClient(db, server_api=ServerApi('1'), tlsCAFile=certifi.where())
        self.db = mongo_client
        try:
            mongo_client.admin.command('ping')

            print("Pinged your deployment. You successfully connected to MongoDB!")
            # Close the client connection
            # mongo_client.close()
            return mongo_client
        except Exception as e:
            print(e)

    def try_to_sign_up(self, user_name, password):
        mongo_client = MongoClient(os.getenv("SECRET_LINK_MONGO_ADMIN"),
                                   tlsCAFile=certifi.where())
        mongo_client.admin.command('createUser', user_name, pwd=password, roles=['readWrite'])
        try:
            mongo_client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            return mongo_client
        except Exception as e:
            print(e)











