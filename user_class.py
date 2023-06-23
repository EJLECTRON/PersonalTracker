#TODO: use decorators fot logging
from pymongo import MongoClient
from tasks_class import TasksForDay

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

    def submit_goal(self, data: str, date: str):
        """
        :param data: task for submit
        :param date: date of showing task
        :return response from db
        """

        tasks_object = TasksForDay()

        response = tasks_object.submit_goal_for_given_date(self, data, date)

        return response


    # TODO: add an error handling to that
    def submitAch(self, data, date):
        pass