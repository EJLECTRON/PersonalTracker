#TODO: use decorators fot logging
from pymongo import MongoClient
from jsonHandler import ConfigHandler

class User:
    def __init__(self, clientName):
        cfg = ConfigHandler()

        cfg.takeCredentialsFromConfig(clientName)

        self.userName = clientName
        self.client = MongoClient(cfg.gatherCredentials())

    # TODO: add an error handling to that
    def submitGoal(self, data, date):
        db = self.client['TestData']

        currentCollection = db[self.userName + "'s tasks"]


    # TODO: add an error handling to that
    def submitAch(self, data, date):
        pass