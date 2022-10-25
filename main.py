"""
Tasks:
For today:
        Code:
        - refactor names of variables
        - add a remainder panel on first tab, which states what I planned to do today
        - add colors
        - admit what I have to do next

        Noncode:
        - decide what kind of statistics I would like to show
        - implement the previous task on app
        - decide how to replace or modify tabs
        - find another way(window) to show and add info

List of undone stuff:
        - add a documentation to the functions
        - change sizes, spacing and so on
        - add a database to storage an information that have submitted (at first storage it in a list)
        - search how to make cool button
        - make a window resizeable with flexible interface

        -- search ho to make a better calendar
        -- add logging system (in future with databases)
        -- if I had an empty space, I would add a cyclic video with capybaras

Done stuff:
        - add date at 1 tab (24.10.22)
        - add local directory to git (24.10.22)
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Application(QtWidgets.QApplication):
    def __init__(self):
        super(Ui_Application, self).__init__([])

        self.setStylesApp()

    def setStylesApp(self):
        styles = """
            QLabel{
                font-size: 20px;
                color: #800000;
            }
        """

        self.setStyleSheet(styles)

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        """ Initializes  window"""
        super().__init__()

        self.setupUi()


    def setupUi(self):
        """ Initializes all objects in app"""
        self.x = 200
        self.y = 150
        self.WIDTH = 1536
        self.HEIGHT = 864

        self.setObjectName("self")
        self.setGeometry(self.x, self.y, self.WIDTH, self.HEIGHT)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.setupTabs()
        self.setupLayouts()
        self.setupLabels()
        self.setupTextEditors()
        self.setupCalenders()
        self.setupButtons()

        self.setCentralWidget(self.centralwidget)

        self.setupText()
        self.tabWidget.setCurrentIndex(0)
        #QtCore.QMetaObject.connectSlotsByName(self)

    def setupLabels(self):
        """ Initializes labels and place it in grid"""
        self.label_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_1.setWordWrap(False)
        self.label_1.setObjectName("label_1")

        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")

        #this text appears only after the achievement has been recorded
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setHidden(True)

        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")

        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 3)

        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)

        self.gridLayout.addWidget(self.label_4, 3, 0, 2, 1)

        self.HBox.addWidget(self.label_5)

        self.HBox_2.addWidget(self.label_6)

    def setupTabs(self):
        """ Initializes tabs and place it in grid"""
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, self.WIDTH, self.HEIGHT))
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")

        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.tabWidget.addTab(self.tab_1, "")
        self.tabWidget.addTab(self.tab_2, "")

    def setupButtons(self):
        self.button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button.resize(50, 50)
        self.button.setObjectName("button")

        self.gridLayout.addWidget(self.button, 3, 0, 1, 1)

        self.button_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_2.resize(50, 50)
        self.button_2.setObjectName("button_2")

        self.gridLayout.addWidget(self.button_2, 3, 1, 1, 1)

        self.button_3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_3.resize(50, 50)
        self.button_3.setObjectName("button_3")

        self.gridLayout_2.addWidget(self.button_3, 1, 0, 1, 1)

    def setupLayouts(self):
        """ Initializes layouts and place it in grid"""
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, self.WIDTH - 100, self.HEIGHT - 100))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(50)
        self.gridLayout.setVerticalSpacing(50)
        self.gridLayout.setObjectName("gridLayout")

        self.HBox = QtWidgets.QHBoxLayout()
        self.gridLayout.addLayout(self.HBox, 0, 1, 1, 1)

        self.VBox = QtWidgets.QVBoxLayout()


        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, self.WIDTH - 100, self.HEIGHT - 100))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(50)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.HBox_2 = QtWidgets.QHBoxLayout()
        self.gridLayout_2.addLayout(self.HBox_2, 0, 0, 1, 1)

    def setupBars(self):
        """ Initializes bars and place it in grid"""
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, self.WIDTH - 100, self.HEIGHT - 100))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

    def setupCalenders(self):
        """ Initializes dates and place it in grid"""
        self.calendar = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.calendar.setObjectName("calendar")

        self.calendar_2 = QtWidgets.QCalendarWidget(self.gridLayoutWidget_2)
        self.calendar_2.setObjectName("calendar_2")

        self.HBox.addWidget(self.calendar)

        self.HBox_2.addWidget(self.calendar_2)

    def setupTextEditors(self):
        """ Initializes text editors and place it in grid"""
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.resize(100, 200)
        self.textEdit.setObjectName("textEdit")


        self.textEdit_2 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_2.resize(100, 200)
        self.textEdit_2.setObjectName("textEdit_2")

        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 1)

        self.gridLayout.addWidget(self.textEdit_2, 2, 1, 1, 1)

        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser.resize(200, 100)
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.gridLayout_2.addWidget(self.textBrowser, 2, 0, 1, 1)

        self.gridLayout_2.addWidget(self.textBrowser_2, 1, 1, 1, 1)

    def setupText(self):
        """ Sets text of all widgets"""
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "PersonalApp"))
        self.label_1.setText(_translate("MainWindow", "Share with me your achievement"))
        self.label_2.setText(_translate("MainWindow", "Note: If you want to see your history then move to the next tab"))

        self.label_5.setText(_translate("MainWindow", "Set your goal for the following day:"))

        self.label_4.setText(_translate("MainWindow", "Achievement has been recorded"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Tab 1"))

        self.label_3.setText(_translate("MainWindow", "There'll be some statistics"))
        self.label_6.setText(_translate("MainWindow", "Select date or range of dates ot see your history:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

        self.textEdit.setText(_translate("MainWindow", "That is first textEdit"))
        self.textEdit_2.setText(_translate("MainWindow", "That is second textEdit"))

        self.button.setText(_translate("MainWindow", "Submit a result"))
        self.button_2.setText(_translate("MainWindow", "Submit a goal"))
        self.button_3.setText(_translate("MainWindow", "Search"))




if __name__ == "__main__":
    app = Ui_Application()

    window = Ui_MainWindow()

    window.show()

    app.exec()