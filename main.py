from main_app import Ui_Application, MainWindow
from start_view import StartWindow
from user_class import User

LOGIN_NAME = 'login'
LOGIN_PASSWORD = 'F5YMtBhoIdLuHjog'


if __name__ == "__main__":
    app = Ui_Application()

    start_window = StartWindow()

    start_window.show()

    app.exec()

