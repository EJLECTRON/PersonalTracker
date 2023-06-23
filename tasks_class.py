from pymongo.errors import OperationFailure
from user_class import User

class TasksForDay:

    @staticmethod
    def submit_goal_for_given_date(user: User, data: str, date: str):
        """
        Submit task for given date for given user
        :param user: current user
        :param data: data to submit
        :param date: date in text format '%d/%m/%Y'
        :return:
        """
        pass


    @staticmethod
    def get_tasks_for_given_date(user: User, date: str):
        """
        Get tasks for given date for given user

        :param user: current user
        :param date: date in text format '%d/%m/%Y'
        :return: tuple of tasks
        """
        tasks_for_given_date = TasksForDay().__extract_tasks_for_given_date(user, date)

        return tasks_for_given_date

    @staticmethod
    def __extract_tasks_for_given_date(user: User, date: str):
        """
        Extract tasks of specific user and returns it as a tuple
        :param user:
        :param date:
        :return:
        """
        possible_error, result = None, []

        try:
            db = user.mongo_client[user.get_user_name]
        except OperationFailure:
            possible_error = "Can't connect ot database, report this issue"

            return (possible_error)

        coll_of_tasks = db.tasks.find_one({}, {"_id": 0, date: 1})

        try:
            for name_of_task, task in coll_of_tasks[date].items():
                result.append(task)
        except (KeyError, TypeError):
            possible_error = f"Error: tasks for {date} wasn't found"

            return (possible_error)

        return tuple(result)