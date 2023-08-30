from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from ui_reportError import Ui_Dialog
from uuid import uuid4
def generate_id_of_error():
    id = str(uuid4())

    return id

class ErrorDialog(QtWidgets.QDialog):
    def __init__(self, text_of_error = "Unknown problem"):
        QtWidgets.QDialog.__init__(self)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.id = generate_id_of_error()

        self.__insertIdIntoLabel(self.id)

        self.__insert_text_of_error_into_label(text_of_error)

        self.__buttonActions()

    def __buttonActions(self):
        pass

    def __insertIdIntoLabel(self, id):
        _translate = QtCore.QCoreApplication.translate

        self.ui.idLabel.setText(_translate("Dialog", "Error id: " + id))

    def __insert_text_of_error_into_label(self, text):
        _translate = QtCore.QCoreApplication.translate

        self.ui.errorLabel.setText(_translate("Dialog", "The text of the error: " + text))

    def __send_issue(self):
        pass


class MessageAlert(QtWidgets.QMessageBox):
    def __init__(self, text):
        QtWidgets.QMessageBox.__init__(self)

        self.setWindowTitle("Alert message")

        self.setWindowIcon(QIcon('icons/icons8-information-50.png'))

        self.set_text_of_message(text)

    def set_text_of_message(self, text):
        self.setText(text)


class CustomDialog(QtWidgets.QDialog):
    def __init__(self, message):
        super().__init__()
        self.entered_code = None

        self.setWindowTitle("Alert")
        self.setWindowIcon(QIcon('icons/icons8-information-50.png'))
        self.setMinimumWidth(300)

        layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel(message)
        layout.addWidget(label)

        self.line_edit = QtWidgets.QLineEdit()
        layout.addWidget(self.line_edit)

        self.ok_button = QtWidgets.QPushButton("OK")
        layout.addWidget(self.ok_button)

        self.ok_button.clicked.connect(self.read_code)  # Connect the signal to the function

        self.setLayout(layout)

    def read_code(self):
        entered_text = self.line_edit.text()
        self.entered_code = entered_text
        self.accept()

