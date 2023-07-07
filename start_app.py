from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from ui_startInterface import *

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
        self.ui.createAccountBtn.clicked.connect(self.__switch_to_log_in)
        self.ui.closeWindowBtn.clicked.connect(self.__close_window)
        self.ui.collapseWindowBtn.clicked.connect(self.__hide_window)

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