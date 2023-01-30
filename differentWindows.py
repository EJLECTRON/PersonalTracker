from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from ui_reportError import Ui_Dialog
from uuid import uuid4

class ErrorDialog(QtWidgets.QDialog):
    def __init__(self, textOfError = "Unknown problem"):
        QtWidgets.QDialog.__init__(self)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.id = self.__generateId()

        self.__insertIdIntoLabel(self.id)

        self.__insertTextOfErrorIntoLabel(textOfError)

        self.__buttonActions()

    def __buttonActions(self):
        pass

    def __insertIdIntoLabel(self, id):
        _translate = QtCore.QCoreApplication.translate

        self.ui.idLabel.setText(_translate("Dialog", "Error id: " + id))

    def __insertTextOfErrorIntoLabel(self, text):
        _translate = QtCore.QCoreApplication.translate

        self.ui.errorLabel.setText(_translate("Dialog", "The text of the error: " + text))

    def __generateId(self):
        id = str(uuid4())

        return id

    def __sendIssue(self):
        pass


class MessageAlert(QtWidgets.QMessageBox):
    def __init__(self, text):
        QtWidgets.QMessageBox.__init__(self)

        self.setWindowTitle("Alert message")

        self.setWindowIcon(QIcon('icons/icons8-information-50.png'))

        self.setText(text)