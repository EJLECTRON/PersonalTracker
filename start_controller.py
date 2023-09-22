from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets

from user_class import User
from start_model import StartModel
from different_windows import MessageAlert, CustomDialog


class StartController:
    """ Custom class for start window"""
    def __init__(self, _view, _program_handler):
        self._model = StartModel()
        self._view = _view
        self._program_handler = _program_handler

    def show_quote(self):
        """ Shows a random quote from quotes.start_quotes in the _view widget """
        quote = self._model.get_quote()
        self._view.ui.quoteLabel.setText(quote)

    def clear_log_in(self):
        """ Clears log in line edit in the _view widget """
        self._view.ui.logInLineEdit.clear()
        self._view.ui.passwordLineEdit.clear()

    def clear_sign_up(self):
        """ Clears sign up line edit in the _view widget """
        self._view.ui.usernameLineEdit.clear()
        self._view.ui.newEmailLineEdit.clear()
        self._view.ui.newPasswordLineEdit.clear()
        self._view.ui.repeatPasswordLineEdit.clear()


    # -----------button functions------------------------------------
    def log_in(self):
        given_user_name = self._view.ui.logInLineEdit.text()
        given_password = self._view.ui.passwordLineEdit.text()

        self._model.user_name = given_user_name
        self._model.password = given_password
        result = None

        if self._model.is_correct_data_for_log_in() == 10:
            result = self._model.try_to_log_in()

        if result:
            self.close_window_and_launch_main_app()
        else:
            self.alert_message = MessageAlert("User was not found, try again")
            self.alert_message.show()

            self.clear_log_in()

    def sign_up(self):
        user_name = self._view.ui.usernameLineEdit.text()
        password = self._view.ui.newPasswordLineEdit.text()
        user_email = self._view.ui.newEmailLineEdit.text()
        repeated_password = self._view.ui.repeatPasswordLineEdit.text()

        self._model.user_name = user_name
        self._model.password = password
        self._model.user_email = user_email
        self._model.repeated_password = repeated_password
        response = self._model.is_correct_data_for_sign_up()
        if response == 10:
            response = self._model.try_to_sign_up()
        if response == 11:
            self.show_alert_message("Not all necessary information provided")
        elif response == 12:
            self.show_alert_message("Username mustn't contain '.' or '$' symbols ")
        elif response ==13:
            self.show_alert_message("Make sure repeated password is the same as password")
        elif response == 2:
            self._view.ui.mainBody.setCurrentIndex(0)
            self.show_alert_message("Username is occupied, try another username")
        elif response == 3:
            self.show_alert_message("Error verifying e-mail address")
        elif response == 5:
            self.show_alert_message("E-mail is occupied, try another e-mail")
        else:
            self.custom_dialog = CustomDialog("Enter code from email")
            self.custom_dialog.show()
            if self.custom_dialog.exec_() == QtWidgets.QDialog.Accepted:
                if response == self.custom_dialog.entered_code:
                    self._model.add_new_user()
                    self.show_alert_message("User created successfully")
                    self.clear_sign_up()
                else:
                    self.show_alert_message("Wrong code, try again")

    def show_alert_message(self, message):
        self.alert_message = MessageAlert(message)
        self.alert_message.show()
    def switch_to_new_user(self):
        """ switch to the new user window in the _view widget """
        self._view.ui.mainBody.setCurrentIndex(1)

    def switch_to_log_in(self):
        """ switch to the log in window in the _view widget """
        self._view.ui.mainBody.setCurrentIndex(0)

    def forgot_password(self):
        """ waiting for implementation """
        self.alert_message = MessageAlert("Try to remember it )")
        self.alert_message.show()

    def hide_tool_tip(self):
        """ hide tool tip"""
        self._view.setWindowFlag(Qt.FramelessWindowHint)

    def hide_window(self):
        """ hide window"""
        self._view.showMinimized()

    def close_window(self):
        """ close window"""
        self._view.close()

    def close_window_and_launch_main_app(self):
        """ close window and launch main app"""
        self._view.close()
        self._program_handler.close_start_and_show_main_window(User(self._model.user_name, self._model.password))













