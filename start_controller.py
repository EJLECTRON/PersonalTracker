from PyQt5.QtCore import Qt
from start_model import StartModel
from different_windows import MessageAlert, CustomDialog


class StartController:
    """ Custom class for start window"""
    def __init__(self, _view):
        self._model = StartModel()
        self._view = _view

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

        if self._model.is_correct_data_for_log_in():
            result = self._model.try_to_log_in()

        if result:
            self.close_window_and_launch_main_app()
        else:
            self.alert_message = MessageAlert("User has not found, try again")
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
        response = 4
        if self._model.is_correct_data_for_sign_up():
            response = self._model.try_to_sign_up()

        elif response == 1:
            self.alert_message = MessageAlert("Not all necessary information provided")
            self.alert_message.show()
        if response == 2:
            self._view.ui.mainBody.setCurrentIndex(0)
            self.alert_message = MessageAlert("Username is occupied, try another username")
            self.alert_message.show()
        elif response == 3:
            self.alert_message = MessageAlert("Error verifying e-mail address")
            self.alert_message.show()
        else:
            self.custom_dialog = CustomDialog("Enter code from email")
            self.custom_dialog.show()
            if response == self.custom_dialog.line_edit.text():
                self._model.add_new_user()
                self.alert_message = MessageAlert("User created successfully")
                self.alert_message.show()
                self.clear_sign_up()
            else:
                self.alert_message = MessageAlert("Wrong code. Try registering again")
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

        return 'donut'









