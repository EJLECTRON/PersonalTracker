from PyQt5.QtWidgets import QWidget

from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from ui_startInterface import Ui_Form
from start_model import StartModel

class StartWindow(QtWidgets.QWidget):
    """ Custom class for start window"""

    def __init__(self):
        QWidget.__init__(self)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        try:
            self.__button_actions()
            self.__hide_tool_tip()
        except Exception as error:
            print(error)

    def __button_actions(self):
        """ setting up all actions for buttons"""
        self.ui.newUserBtn.clicked.connect(self.__switch_to_new_user)

        self.ui.closeWindowBtn.clicked.connect(self.__close_window)
        self.ui.collapseWindowBtn.clicked.connect(self.__hide_window)
        self.ui.signInBtn.clicked.connect(self.__log_in)
        self.ui.createAccountBtn.clicked.connect(self.__sign_up)


# -----------buttons functions------------------------------------
    def __switch_to_new_user(self):
        """ switch to new user window"""
        self.ui.mainBody.setCurrentIndex(1)

    def __switch_to_log_in(self):
        """ switch to log in window"""
        self.ui.mainBody.setCurrentIndex(0)

    def __hide_tool_tip(self):
        """ hide tool tip"""
        self.setWindowFlag(Qt.FramelessWindowHint)

    def __hide_window(self):
        """ hide window"""
        self.showMinimized()

    def __close_window(self):
        """ close window"""
        self.close()

    def __close_window_open_main_window(self):
        self.close()


    def __log_in(self):
        user_name = self.ui.logInLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        start = StartModel()
        result = start.try_to_log_in(user_name, password)
        if result != None:
            self.__close_window_open_main_window()

        else:
            QtWidgets.QMessageBox.about(self, "Error", "User not found, try again or create new user")
            print(f"User {user_name} not found")


    def __sign_up(self):
        user_name = self.ui.usernameLineEdit.text()
        password = self.ui.newPasswordLineEdit.text()
        repeated_password = self.ui.repeatPasswordLineEdit.text()
        start = StartModel()
        start.try_to_sign_up(user_name, password, repeated_password)
