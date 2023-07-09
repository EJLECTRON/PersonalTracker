import os
from dotenv import load_dotenv


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

    def try_to_log_in(self, mongo_client):
        return self.try_to_ping(mongo_client)

    def try_to_sign_up(self, mongo_client):
        return self.try_to_ping(mongo_client)











