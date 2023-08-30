from main_model import MainModel
from tasks_class import TasksForDay
from user_class import User


class MainController:
    def __init__(self, _view, user: User):
        """
        :param _view: main window
        :param user: user object
        :param tasks_for_today: class to get tasks for today
        """

        self._model = MainModel(user)
        self._view = _view
        self.tasks_for_today = TasksForDay()

    def submit_goal(self, data: str, date: str):
        response = self._model.try_to_submit_goal(data, date)
        return response

    def get_quote(self):
        quote = self._model.try_to_get_quote()
        return quote