from main_view import Ui_Application, MainWindow
from start_view import StartWindow
from user_class import User

class ProgramHandler:
    LOGIN_NAME = 'login'
    LOGIN_PASSWORD = 'F5YMtBhoIdLuHjog'
    def __init__(self):
        self.start_window = StartWindow(self)
        self.main_window = MainWindow()

    def show_start_window(self):
        self.start_window.show()

    def close_start_and_show_main_window(self, user: User):
        self.main_window.initialize_functionality(User(self.LOGIN_NAME, self.LOGIN_PASSWORD))
        self.main_window.show()

if __name__ == "__main__":
    app = Ui_Application()

    program_handler = ProgramHandler()

    program_handler.show_start_window()


    app.exec()
