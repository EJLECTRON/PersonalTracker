import unittest
from tasks_class import TasksForDay
from user_class import User


class TestSubmitGoals(unittest.TestCase):
    def test_submit_goals(self):
        user = User('login', 'F5YMtBhoIdLuHjog')
        #self.assertEqual(TasksForDay().submit_goal_for_given_date(user, "qr", "23/06/2023"), "Task was successfully submitted", "Can't submit goals")
