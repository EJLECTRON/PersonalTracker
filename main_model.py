from user_class import User
from random import randint


class MainModel:

    def __init__(self, user: User):
        self._user = user

    def try_to_submit_goal(self, data: str, date: str):
        """
        :param data: task for submit
        :param date: date of showing task
        :return response from db
        """
        response = self._user.submit_goal(data, date)
        return response

    def try_to_get_quote(self):
        """
        Get quote from database
        :return: random quote from database
        """
        db = self._user.mongo_client.quotes

        key = randint(1, 35)

        quote = db.Quotes.find_one({str(key): {"$exists": True}}, {"_id": 0})

        return quote[str(key)]