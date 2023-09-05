#TODO: use decorators fot logging
from pymongo import MongoClient

class User:
    def __init__(self, user_name: str, password: str):
        """
        :param user_name: name of a user to access to his db
        :param password: password to make a connection to his db
        """
        self._user_name = user_name
        connection_string = f"mongodb+srv://{self._user_name}:{password}@personalappcluster.vglojvm.mongodb.net/test"
        self.mongo_client = MongoClient(connection_string)

    @property
    def get_user_name(self):
        return self._user_name