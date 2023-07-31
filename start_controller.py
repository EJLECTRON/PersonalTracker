from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from start_model import StartModel


class StartController():
    """ Custom class for start window"""
    def __init__(self, parent):
        self._model = StartModel()
        self.parent = parent

    @staticmethod
    def try_to_ping(mongo_client):
        try:
            mongo_client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            return mongo_client
        except Exception as e:
            print(e)

    def try_to_log_in(self, mongo_client):
        return self.try_to_ping(mongo_client)

    def show_quote(self):
        """ Shows a random quote from quotes.start_quotes in the parent widget """
        quote = self._model.get_quote()
        self.parent.ui.quoteLabel.setText(quote)

    def try_to_sign_up(self, mongo_client):
        return self.try_to_ping(mongo_client)

    # -----------button functions------------------------------------
    def switch_to_new_user(self):
        """ switch to the new user window in the parent widget """
        self.parent.ui.mainBody.setCurrentIndex(1)

    def switch_to_log_in(self):
        """ switch to the log in window in the parent widget """
        self.parent.ui.mainBody.setCurrentIndex(0)

    def hide_tool_tip(self):
        """ hide tool tip"""
        self.parent.setWindowFlag(Qt.FramelessWindowHint)

    def hide_window(self):
        """ hide window"""
        self.parent.showMinimized()

    def close_window(self):
        """ close window"""
        self.parent.close()

    def close_window_open_main_window(self):
        self.parent.close()

    def log_in(self):
        user_name = self.parent.ui.logInLineEdit.text()
        password = self.parent.ui.passwordLineEdit.text()

        start = StartModel(user_name, password)
        result = None

        if start.is_correct_data_for_log_in():
            result = start.try_to_log_in()

        if result is not None:
            self.close_window_open_main_window()
        else:
            QtWidgets.QMessageBox.about(self.parent.ui, "Error", "User not found, try again or create new user")
            print(f"User {user_name} not found")


    def sign_up(self):
        user_name = self.parent.ui.usernameLineEdit.text()
        password = self.parent.ui.newPasswordLineEdit.text()
        repeated_password = self.parent.ui.repeatPasswordLineEdit.text()
        self._model = StartModel(user_name, password, repeated_password)
        start = self._model.is_correct_data_for_log_in()

        if start.is_correct_data_for_sign_up():
            start.try_to_sign_up()













