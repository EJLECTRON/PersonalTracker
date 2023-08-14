from PyQt5.QtCore import Qt
from start_model import StartModel
from different_windows import MessageAlert


class StartController:
    """ Custom class for start window"""
    def __init__(self, parent):
        self._model = StartModel()
        self.parent = parent

    def log_in(self):
        given_user_name = self.parent.ui.logInLineEdit.text()
        given_password = self.parent.ui.passwordLineEdit.text()

        self._model.user_name = given_user_name
        self._model.password = given_password
        result = None

        if self._model.is_correct_data_for_log_in():
            result = self._model.try_to_log_in()

        if result:
            self.close_window()
        else:
            self.alert_message = MessageAlert("User not found, try again")
            self.alert_message.show()

    def sign_up(self):
        user_name = self.parent.ui.usernameLineEdit.text()
        password = self.parent.ui.newPasswordLineEdit.text()
        repeated_password = self.parent.ui.repeatPasswordLineEdit.text()

        self._model.user_name = user_name
        self._model.password = password
        self._model.repeated_password = repeated_password

        response = None

        if self._model.is_correct_data_for_sign_up():
            response = self._model.try_to_sign_up()

        if response:
            self.parent.ui.mainBody.setCurrentIndex(0)
            self.alert_message = MessageAlert("User was created, now you can log in")
            self.alert_message.show()
        else:
            self.alert_message = MessageAlert("Username is occupied, try again")
            self.alert_message.show()


    def show_quote(self):
        """ Shows a random quote from quotes.start_quotes in the parent widget """
        quote = self._model.get_quote()
        self.parent.ui.quoteLabel.setText(quote)

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













