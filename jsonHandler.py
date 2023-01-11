import json

class ConfigHandler(object):
    def __init__(self):
        with open("data/databaseconfig.json") as cfg:
            data = json.load(cfg)

            self.start = data['start']
            self.end = data['end']

        self.user = "none"
        self.password = "none"

    def takeCredentialsFromConfig(self, clientname):
        with open("data/databaseconfig.json") as cfg:
            data = json.load(cfg)

            try:
                self.user = clientname
                self.password = data['users'][clientname]
            except KeyError:
                print("There is no such client")

    def gatherCredentials(self):
        return self.start + self.user + ":" + self.password + self.end



def takeInfointoList(name):
    pass