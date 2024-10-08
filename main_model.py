from user_class import User
from error_class import ErrorIntoUI

from random import randint
from pymongo.errors import OperationFailure


class MainModel:

    def __init__(self, user: User):
        self._user = user
    
    def try_to_get_tasks_for_given_date(self, date: str):
        """
        Get tasks for day
        :param date: date in text format '%d/%m/%Y'
        :return: tuple of tasks
        """
        tasks_for_today = self.__log_in_and_extract_tasks_for_given_date(self._user, date)
        return tasks_for_today

    def try_to_submit_goal_for_given_date(self, data: str, date: str):
        """
        :param data: task for submit
        :param date: date of showing task
        :return response from db
        """
        response = self.__log_in_and_submit_tasks_for_given_date(self._user, data, date)
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

    def __log_in_and_submit_tasks_for_given_date(self, user, data: str, date: str):
        """
        :param user: current user (type: User from user_class.py)
        :param data: given tasks
        :param date: date in text format '%d/%m/%Y'
        :return: response from db
        """

        db = self.logging_to_user_db()

        if db is not None:
            try:
                status = db.tasks.find_one_and_update({date: {'$exists': True}}, {"$push": {date: data}})

                if status is None:
                    db.tasks.insert_one({date: [data]})

                return "Task was successfully submitted"
            except OperationFailure:
                possible_error = f"Error: can't submit task for {date}, report this issue"

                ErrorIntoUI(possible_error)

    def __log_in_and_extract_tasks_for_given_date(self, user, date: str):
        """
        Extract tasks of specific user and returns it as a tuple
        :param user: current user (type: User from user_class.py)
        :param date: date in text format '%d/%m/%Y'
        :return: tuple of tasks
        """
        db = self.logging_to_user_db()

        if db is not None:
            cursor_object_of_tasks_for_given_date = db.tasks.find_one({date: {'$exists': True}}, {"_id": 0})

            result = self.__extract_tasks_for_given_date(cursor_object_of_tasks_for_given_date, date)

            return result

    def __extract_tasks_for_given_date(self, cursor_object_of_tasks_for_given_date, date: str):
        """
        Extract tasks for given date from cursor object
        :param cursor_object_of_tasks_for_given_date:
                type: Cursor,
                it's a dict with date as a key and list of tasks as a value
        :param date: date in text format '%d/%m/%Y'
        :return: tuple of tasks
        """
        result = []

        try:
            for task in cursor_object_of_tasks_for_given_date[date]:
                result.append(task)
        except (KeyError, TypeError):
            result = f"Error: tasks for {date} wasn't found"

            ErrorIntoUI(result)

        return (result, "")

    def logging_to_user_db(self):
        """
        Logging to user db
        :return: connection to user db or None if error
        """
        try:
            db = self._user.mongo_client[self._user.get_user_name]

            return db
        except OperationFailure:
            possible_error = "Can't connect ot database, report this issue"

            ErrorIntoUI(possible_error)
            
    @property
    def user(self):
        return self._user