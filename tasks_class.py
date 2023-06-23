from pymongo.errors import OperationFailure
from error_class import ErrorIntoUI

class TasksForDay:

    @staticmethod
    def submit_goal_for_given_date(user, data: str, date: str):
        """
        Submit task for given date for given user
        :param user: current user
        :param data: data to submit
        :param date: date in text format '%d/%m/%Y'
        :return:
        """
        pass


    @staticmethod
    def get_tasks_for_given_date(user, date: str):
        """
        Get tasks for given date for given user

        :param user: current user
        :param date: date in text format '%d/%m/%Y'
        :return: tuple of tasks
        """
        tasks_for_given_date = TasksForDay().__log_in_and_extract_tasks_for_given_date(user, date)

        return tasks_for_given_date

    def __log_in_and_extract_tasks_for_given_date(self, user, date: str):
        """
        Extract tasks of specific user and returns it as a tuple
        :param user: current user (type: User from user_class.py)
        :param date: date in text format '%d/%m/%Y'
        :return: tuple of tasks
        """
        db = self.logging_to_user_db(user)

        if db:
            coll_of_tasks = db.tasks.find_one({}, {"_id": 0, date: 1})

            result = self.__extract_tasks_for_given_date(coll_of_tasks, date)

            return result

    def __extract_tasks_for_given_date(self, coll_of_tasks, date: str):
        result = []

        try:
            for name_of_task, task in coll_of_tasks[date].items():
                result.append(task)
        except (KeyError, TypeError):
            possible_error = f"Error: tasks for {date} wasn't found"

            ErrorIntoUI(possible_error)

        return tuple(result)

    @staticmethod
    def logging_to_user_db(user):
        """
        Logging to user db
        :param user: user to log in
        :return: connection to user db or None if error
        """
        try:
            db = user.mongo_client[user.get_user_name]

            return db
        except OperationFailure:
            possible_error = "Can't connect ot database, report this issue"

            ErrorIntoUI(possible_error)