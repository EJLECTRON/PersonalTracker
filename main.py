from main_app import Ui_Application, MainWindow
from user_class import User
from hashlib import sha256

LOGIN_NAME = 'login'
LOGIN_PASSWORD = 'F5YMtBhoIdLuHjog'

def get_hashed_password(password: str):
    pass

def get_credentials_of_user(user_name: str, user_password: str):
    pass

if __name__ == "__main__":
    temp_client = User(LOGIN_NAME, LOGIN_PASSWORD)
    user_name, user_password = 'Mykola', 'that_is_s0me_password'
    app = Ui_Application()

    mainWindow = MainWindow(temp_client)

    mainWindow.show()

    app.exec()