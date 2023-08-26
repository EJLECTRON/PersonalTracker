from main_view import Ui_Application, MainWindow
from start_view import StartWindow
from user_class import User

LOGIN_NAME = 'login'
LOGIN_PASSWORD = 'F5YMtBhoIdLuHjog'


if __name__ == "__main__":
    app = Ui_Application()

    user = User(LOGIN_NAME, LOGIN_PASSWORD)
    login_window = StartWindow()
    start_window = MainWindow(user)

    start_window.show()
    login_window.show()

    app.exec()