#TO DO: Add - _alert_message: MessageAlert
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QPoint
from PyQt5 import QtWidgets
from ui_startInterface import Ui_Form
from start_controller import StartController


class StartWindow(QtWidgets.QWidget):
    """ Custom class for start window"""

    def __init__(self):
        QWidget.__init__(self)
        QtWidgets.QWidget.__init__(self)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.old_pos = self.pos()
        self.controller = StartController(self)

        try:
            self.__button_actions()
            self.controller.hide_tool_tip()
            self.controller.show_quote()
        except Exception as error:
            print(error)

    def mousePressEvent(self, event):
        """ mouse press event that updates old position of window"""
        self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        """ mouse move event that moves window"""
        delta = QPoint(event.globalPos() - self.old_pos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_pos = event.globalPos()

    def __button_actions(self):
        """ setting up all actions for buttons"""
        self.ui.newUserBtn.clicked.connect(self.controller.switch_to_new_user)
        self.ui.closeWindowBtn.clicked.connect(self.controller.close_window)
        self.ui.collapseWindowBtn.clicked.connect(self.controller.hide_window)
        self.ui.signInBtn.clicked.connect(self.controller.log_in)
        self.ui.createAccountBtn.clicked.connect(self.controller.sign_up)
        self.ui.returnToMenuBtn.clicked.connect(self.controller.switch_to_log_in)

