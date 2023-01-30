#TODO: use decorators fot logging
from pymongo import MongoClient
from jsonHandler import ConfigHandler

class User:
    def __init__(self, clientName):
        cfg = ConfigHandler()

        cfg.takeCredentialsFromConfig(clientName)

        self.userName = clientName
        self.client = MongoClient(cfg.gatherCredentials())
