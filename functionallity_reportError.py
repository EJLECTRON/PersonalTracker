from PyQt5 import QtWidgets, QtCore
from ui_reportError import Ui_Dialog
from uuid import uuid4

class ErrorDialog(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.id = self.__generateId()

        self.__insertIdIntoLabel(self.id)

        self.__buttonActions()

        self.show()

    def __buttonActions(self):
        pass

    def __insertIdIntoLabel(self, id):
        _translate = QtCore.QCoreApplication.translate

        self.ui.idLabel.setText(_translate("Dialog", "Error id: " + id))

    def insertTextOfErrorIntoLabel(self, text):
        pass

    def __generateId(self):
        id = str(uuid4())

        return id

    def __sendIssue(self):
        pass


