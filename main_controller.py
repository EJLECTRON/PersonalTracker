from main_model import MainModel
from user_class import User


class MainController:
    def __init__(self, _view, user: User):
        """
        :param _view: main window
        :param user: user object
        """

        self._model = MainModel(user)
        self._view = _view

    def get_tasks_for_day(self, date: str):
        """
        Get tasks for day
        :param date: date in text format '%d/%m/%Y'
        :return: tuple of tasks
        """
        tasks_for_today = self._model.try_to_get_tasks_for_given_date(date)
        return tasks_for_today

    def submit_goal(self, data: str, date: str):
        response = self._model.try_to_submit_goal_for_given_date(data, date)
        return response

    def get_quote(self):
        quote = self._model.try_to_get_quote()
        return quote