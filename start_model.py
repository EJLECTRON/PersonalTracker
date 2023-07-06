from ui_startInterface import *
from start_controller import StartController

# for .env
import os
from dotenv import load_dotenv
class StartModel(QtWidgets.QWidget):
    """ Custom class for start window"""

    def __init__(self):
        load_dotenv()

        super().__init__()
        self.user_name = None
        self.password = None
        self.repeated_password = None
        self.db = None
        self.controller = StartController()

    def try_to_log_in(self, user_name, password):
        self.user_name = user_name
        self.password = password
        if self.user_name != None and self.password != None:
            self.db = os.getenv("LINK_ADD_USER_PART1") + user_name + ":" + password + os.getenv("LINK_ADD_USER_PART2")
            return self.controller.try_to_log_in(self.db)
        else:
            return False

    def try_to_sign_up(self, user_name, password, repeated_password):
        if user_name != None and password == repeated_password and password != None:
            self.user_name = user_name
            self.password = password
            self.db = os.getenv("LINK_ADD_USER_PART1") + user_name + ":" + password + os.getenv("LINK_ADD_USER_PART2")
            result = self.controller.try_to_sign_up(user_name, password)
            return result

    """
    def create_main_window(self):
        temp_client = User(self.username, self.password)
        main_window = MainWindow(temp_client)
        main_window.show()
    """







