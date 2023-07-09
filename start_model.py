import os
from dotenv import load_dotenv
from ui_startInterface import *
from start_controller import StartController



class StartModel(QtWidgets.QWidget):
    """ Custom class for start window"""

    def __init__(self, user_name=None, password=None, repeated_password=None):
        load_dotenv()

        super().__init__()
        self.user_name = user_name
        self.password = password
        self.repeated_password = repeated_password
        self.controller = StartController()

    def is_correct_data_for_log_in(self):
        """ checks if given data to model is correct to log in to db"""
        return self.user_name is not None and self.password is not None and self.user_name != "" and self.password != ""

    def is_correct_data_for_sign_up(self):
        """ checks if given data to model is correct to sign up to db"""
        return self.is_correct_data_for_log_in() and self.password == self.repeated_password

    def try_to_log_in(self):
        db = os.getenv("LINK_ADD_USER_PART1") + self.user_name + ":" + self.password + os.getenv("LINK_ADD_USER_PART2")
        return self.controller.try_to_log_in(db)


    def try_to_sign_up(self):
        #db = os.getenv("LINK_ADD_USER_PART1") + self.user_name + ":" + self.password + os.getenv("LINK_ADD_USER_PART2")
        result = self.controller.try_to_sign_up(self.user_name, self.password)
        return result

    """
    def create_main_window(self):
        temp_client = User(self.username, self.password)
        main_window = MainWindow(temp_client)
        main_window.show()
    """







