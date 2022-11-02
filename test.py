from PyQt5 import QtCore, QtWidgets

def _setupButtons(self):
    self.buttonSubmitAch = self._createButton(self.tab1gridLayoutW, "buttonSubmitAch", 50, 50)
    self.tab1gridLayout.addWidget(self.buttonSubmitAch, 3, 0, 1, 1)

    self.buttonSubmitGoal = self._createButton(self.tab1gridLayoutW, "buttonSubmitGoal", 50, 50)
    self.tab1gridLayout.addWidget(self.buttonSubmitGoal, 3, 1, 1, 1)

    self.buttonSearch = self._createButton(self.tab1gridLayoutW, "buttonSearch", 50, 50)
    self.tab2gridLayout.addWidget(self.buttonSearch, 1, 0, 1, 1)


def _setupLayouts(self):
    """ Initializes layouts and place it in grid"""
    self.tab1gridLayoutW = QtWidgets.QWidget(self.tab_1)
    self.tab1gridLayoutW.setGeometry(QtCore.QRect(0, 0, self.WIDTH - 100, self.HEIGHT - 100))
    self.tab1gridLayoutW.setObjectName("tab1gridLayoutW")

    self.tab1gridLayout = QtWidgets.QGridLayout(self.tab1gridLayoutW)
    self.tab1gridLayout.setContentsMargins(0, 0, 0, 0)
    self.tab1gridLayout.setHorizontalSpacing(50)
    self.tab1gridLayout.setVerticalSpacing(50)
    self.tab1gridLayout.setObjectName("tab1gridLayout")

    self.tab1HBox01 = QtWidgets.QHBoxLayout()
    self.tab1gridLayout.addLayout(self.tab1HBox01, 0, 1, 1, 1)

    self.tab1VBox02 = QtWidgets.QVBoxLayout()
    self.tab1gridLayout.addLayout(self.tab1VBox02, 0, 2, 1, 1)

    self.tab2gridLayoutW = QtWidgets.QWidget(self.tab_2)
    self.tab2gridLayoutW.setGeometry(QtCore.QRect(0, 0, self.WIDTH - 100, self.HEIGHT - 100))
    self.tab2gridLayoutW.setObjectName("tab2gridLayoutW")

    self.tab2gridLayout = QtWidgets.QGridLayout(self.tab2gridLayoutW)
    self.tab2gridLayout.setContentsMargins(0, 0, 0, 0)
    self.tab2gridLayout.setHorizontalSpacing(50)
    self.tab2gridLayout.setVerticalSpacing(10)
    self.tab2gridLayout.setObjectName("tab2gridLayout")

    self.tab2HBox00 = QtWidgets.QHBoxLayout()
    self.tab2gridLayout.addLayout(self.tab2HBox00, 0, 0, 1, 1)


def _setupCalenders(self):
    """ Initializes dates and place it in grid"""
    self.tab1Calendar = QtWidgets.QDateEdit(self.tab1gridLayoutW)
    self.tab1Calendar.setObjectName("tab1Calendar")

    self.tab2Calendar = QtWidgets.QCalendarWidget(self.tab2gridLayoutW)
    self.tab2Calendar.setObjectName("tab2Calendar")

    self.tab1HBox01.addWidget(self.tab1Calendar)

    self.tab2HBox00.addWidget(self.tab2Calendar)


def _setupTextEditors(self):
    """ Initializes text editors and place it in grid"""
    self.textEditSubmitAch = self._createTextEdit(self.tab1gridLayoutW, "textEditSubmitAch", 100, 200)

    self.textEditSubmitGoal = self._createTextEdit(self.tab1gridLayoutW, "textEditSubmitGoal", 100, 200)

    self.tab1gridLayout.addWidget(self.textEditSubmitAch, 2, 0, 1, 1)

    self.tab1gridLayout.addWidget(self.textEditSubmitGoal, 2, 1, 1, 1)

    self.textBrowserShow = QtWidgets.QTextBrowser(self.tab2gridLayoutW)
    self.textBrowserShow.resize(200, 100)
    self.textBrowserShow.setObjectName("textBrowserShow")

    self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab2gridLayoutW)
    self.textBrowser_2.setObjectName("textBrowser_2")

    self.tab2gridLayout.addWidget(self.textBrowserShow, 2, 0, 1, 1)

    self.tab2gridLayout.addWidget(self.textBrowser_2, 1, 1, 1, 1)


def _setupGroupBoxes(self):
    "Initializes group boxes and add them to the grid"


def _setupRadioButtons(self):
    """ Initializes radiobuttons for the groupbox"""

    self.radioButton = self._createRadioButton(self.tab1gridLayoutW, "radioButton", "First task")
    self.tab1VBox02.addWidget(self.radioButton)

    self.radioButton_2 = self._createRadioButton(self.tab1gridLayoutW, "radioButton_2", "Second task")
    self.tab1VBox02.addWidget(self.radioButton_2)

    self.radioButton_3 = self._createRadioButton(self.tab1gridLayoutW, "radioButton_3", "Third task")
    self.tab1VBox02.addWidget(self.radioButton_3)