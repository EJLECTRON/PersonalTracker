from PyQt5 import QtWidgets
from ui_startInterface import *

class StartWindow(QtWidgets.QWidget):
    """ Custom class for start window"""

    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        try:
            self.__button_actions()
        except Exception as error:
            print(error)

    def __button_actions(self):
        """ setting up all actions for buttons"""
        self.ui.newUserBtn.clicked.connect(self.__switch_to_new_user)
        self.ui.createAccountBtn.clicked.connect(self.__switch_to_log_in)

# -----------buttons functions------------------------------------
    def __switch_to_new_user(self):
        """ switch to new user window"""
        self.ui.mainBody.setCurrentIndex(1)

    def __switch_to_log_in(self):
        """ switch to log in window"""
        self.ui.mainBody.setCurrentIndex(0)