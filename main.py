"""
Tasks:
    On going:
            Code:
            - add dialog windows
            - add colors
            - remake goals from textedit to radiobuttons
            - admit what I have to do next

            Noncode:
            - take an idea of interface from utorrent
            - decide what kind of statistics I would like to show
            - decide how to replace or modify tabs
            - Search how to work with dialogs windows
            - find another way(window) to show and add info

    List of undone stuff:
            - implement statistics
            - add a better documentation to the functions
            - change sizes, spacing and so on
            - add a database to storage an information that have submitted (at first storage it in a list)
            - search how to make cool button
            - add GIFs
            - make a window resizeable with flexible interface

            -- search ho to make a better calendar
            -- add logging system (in future with databases)
            -- if I had an empty space, I would add a cyclic video with capybaras
"""

# TODO: When you click on calendar: on the first tab you get achievements
#                                  on the second tab you get goals
from PyQt5 import QtCore, QtWidgets
#from PyQt5.uic import loadUiType
from os import path
import sys

class Ui_Application(QtWidgets.QApplication):
    """ Custom class for application"""
    def __init__(self):
        super(Ui_Application, self).__init__([])

        self._setStylesApp()

    def _setStylesApp(self):

        styles = """
            QWidget{
                background-color: #3fc46c;
            }
            
            QLabel{
                font-size: 20px;
                color: #3fc46c;
            }
            
            QPushButton {
                color: #000000;
                background-color: #c46c3f;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                font: bold 14px;
                min-width: 10em;
                padding: 6px;
            }
                 
            QDateEdit {
                color: #3fc46c;
            }
            
            QTextEdit {
                background-color: #ffffff;
            }
            
            QRadioButton {
                color: #3fc46c;
            }
            
            QVBoxLayout {
                background-color: #6c3fc4;
            }
            
            QHBoxLayout {
                background-color: #6c3fc4;
            }
        """

        self.setStyleSheet(styles)

class Ui_MainWindow(QtWidgets.QMainWindow):
    """ Custom class for Main Window"""
    def __init__(self):
        """ Initializes  window"""
        super().__init__()

        self._setupUi()

        self._buttonActions()


# ---------------setup----------------------
    def _setupUi(self):
        """ Initializes all objects in app"""
        self.x = 200
        self.y = 150
        self.WIDTH = 1400
        self.HEIGHT = 900

        self.setObjectName("self")
        self.setGeometry(self.x, self.y, self.WIDTH, self.HEIGHT)

        # have to place it somewhere else
        self.mainWidget = QtWidgets.QWidget(self)
        self.mainWidget.setObjectName("mainWidget")

        self.maingridLayout = self._createLayout(self.mainWidget, "maingridLayout", 50, 50)

        self._setupTabs()
        self._setupLayouts()
        # self._setupLabels()
        self._setupTextEditors()
        self._setupCalendars()
        self._setupButtons()
        self._setupBars()
        # self._setupRadioButtons()

        self.setCentralWidget(self.mainWidget)

        self._setupTexts()
        self.tabWidget.setCurrentIndex(0)

    def _setupLabels(self):
        """ Initializes labels and place it in grid"""
        self.shareLabel = self._createLabel(self.tab1gridLayoutW, "shareLabel")

        self.noteLabel = self._createLabel(self.tab1gridLayoutW, "noteLabel", QtCore.Qt.AlignCenter)

        # this text appears only after the achievement has been recorded
        self.recordedLabel = self._createLabel(self.tab1gridLayoutW, "recordedLabel", True)

        self.setGoalLabel = self._createLabel(self.tab1gridLayoutW, "setGoalLabel")

        self.dateRangeLabel = self._createLabel(self.tab2gridLayoutW, "dateRangeLabel")

        self.tasksToDoLabel = self._createLabel(self.tab1gridLayoutW, "tasksToDoLabel")

        self.statLabel = self._createLabel(self.tab2gridLayoutW, "statLabel")

        self.tab1gridLayout.addWidget(self.shareLabel, 0, 0, 1, 1)

        self.tab1gridLayout.addWidget(self.noteLabel, 5, 0, 1, 2)

        self.tab1gridLayout.addWidget(self.recordedLabel, 3, 0, 2, 1)

        self.tab1HBox01.addWidget(self.setGoalLabel)

        self.tab1VBox02.addWidget(self.tasksToDoLabel)

        self.tab2gridLayout.addWidget(self.statLabel, 0, 1, 1, 1)

        self.tab2HBox00.addWidget(self.dateRangeLabel)

    def _setupTabs(self):
        """ Initializes tabs and place it in grid"""
        self.tabWidget = QtWidgets.QTabWidget(self.mainWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 200, 200))
        # self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")

        self.maingridLayout.addWidget(self.tabWidget, 2, 2, 1, 1)

        self.tab_1 = self._createTab("tab_1")

        self.tab_2 = self._createTab("tab_2")

        self.tabWidget.addTab(self.tab_1, "")
        self.tabWidget.addTab(self.tab_2, "")

    def _setupLayouts(self):
        """ Initializes layouts and place it in grid"""

        self.tab1gridLayoutW = self._createWidget(self.tab_1, "tab1gridLayoutW")

        self.tab1gridLayout = self._createLayout(self.tab1gridLayoutW, "tab1gridLayout", 50, 50,
        0, 0, 0, 0)

        self.tab2gridLayoutW = self._createWidget(self.tab_2, "tab2gridLayoutW", 0, 0,
        self.tab_2.frameGeometry().width(), self.tab_2.frameGeometry().height())

        self.tab2gridLayout = self._createLayout(self.tab2gridLayoutW, "tab2gridLayout", 50, 10,
        0, 0, 0, 0)

    def _setupTextEditors(self):
        """ Initializes text editors and place it in grid"""
        self.textEditSubmitAch = self._createTextEdit(self.mainWidget, "textEditSubmitAch", 100, 200)

        self.textEditSubmitGoal = self._createTextEdit(self.mainWidget, "textEditSubmitGoal", 100, 200)

        self.maingridLayout.addWidget(self.textEditSubmitAch, 0, 0, 1, 1)

        self.maingridLayout.addWidget(self.textEditSubmitGoal, 0, 1, 1, 1)
        # TODO: instead of it make a lot of radiobuttons
        self.textBrowserShow = QtWidgets.QTextBrowser(self.mainWidget)
        self.textBrowserShow.resize(200, 100)
        self.textBrowserShow.setObjectName("textBrowserShow")
        self.textBrowserShow.setReadOnly(True)

        self.maingridLayout.addWidget(self.textBrowserShow, 2, 0, 1, 2)

    def _setupButtons(self):
        """ Initializes buttons and place it in grid"""
        self.buttonSubmitAch = self._createButton(self.mainWidget, "buttonSubmitAch", 50, 50)
        self.maingridLayout.addWidget(self.buttonSubmitAch, 1, 0, 1, 1)

        self.buttonSubmitGoal = self._createButton(self.mainWidget, "buttonSubmitGoal", 50, 50)
        self.maingridLayout.addWidget(self.buttonSubmitGoal, 1, 1, 1, 1)

    def _setupBars(self):
        """ Initializes bars and place it in grid"""
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, self.WIDTH - 100, self.HEIGHT - 100))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

    def _setupCalendars(self):
        self.calendar = QtWidgets.QCalendarWidget(self)

        self.calendar.setObjectName("calendar")

        self.maingridLayout.addWidget(self.calendar, 0, 2, 1, 1)

    def _setupTexts(self):
        """ Sets text of all widgets"""

        _translate = QtCore.QCoreApplication.translate

        self.setWindowTitle(_translate("MainWindow", "PersonalApp"))

        self.textEditSubmitGoal.setText(_translate("MainWindow", "Set your goal for the following day:"))
        self.textBrowserShow.setText(_translate("Main Window", "That is your tasks for today:"))
        self.textEditSubmitAch.setText(_translate("MainWindow", "Share with me your achievement:"))

        """
        self.noteLabel.setText(_translate("MainWindow", "Note: If you want to see your history then move to the next tab"))
        
        self.recordedLabel.setText(_translate("MainWindow", "Achievement has been recorded"))
        self.statLabel.setText(_translate("MainWindow", "There'll be some statistics"))
        self.dateRangeLabel.setText(_translate("MainWindow", "Select date or range of dates to see your history:"))
       
        """
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

        #self.textEditSubmitAch.setDocument(_translate("MainWindow", "Share with me your achievement"))
        #self.textEditSubmitGoal.setDocument(_translate("MainWindow", "That is second textEdit"))

        self.buttonSubmitAch.setText(_translate("MainWindow", "Submit a result"))
        self.buttonSubmitGoal.setText(_translate("MainWindow", "Submit a goal"))
        #self.buttonSearch.setText(_translate("MainWindow", "Search"))


#--------------addition to setup------------------------------

    def _createWidget(self, *args):
        """ Creates a widget in order to put it into a layout and customises it.
        This function supports different number of arguments:
        6 args(QObject, name, x, y, width, height)
        """
        widget = None

        match len(args):
            case 2:
                widget = QtWidgets.QWidget(args[0])
                widget.setObjectName(args[1])

            case 6:
                widget = QtWidgets.QWidget(args[0])
                widget.setObjectName(args[1])
                widget.setGeometry(QtCore.QRect(args[2], args[3], args[4], args[5]))

        return widget

    def _createTab(self, name):
        tab = QtWidgets.QWidget()
        tab.setObjectName(name)

        return tab

    def _createLayout(self, *args):
        """ Creates a layout and customises it.
        This function supports different number of arguments:
        8 args(QWidget, name, horizontal alignment, vertical alignment, left, top, right, bottom)
        """
        layout = None

        match len(args):
            case 2:
                layout = QtWidgets.QGridLayout(args[0])
                layout.setObjectName(args[1])

            case 4:
                layout = QtWidgets.QGridLayout(args[0])
                layout.setObjectName(args[1])
                layout.setHorizontalSpacing(args[2])
                layout.setVerticalSpacing(args[3])

            case 8:
                layout = QtWidgets.QGridLayout(args[0])
                layout.setObjectName(args[1])
                layout.setHorizontalSpacing(args[2])
                layout.setVerticalSpacing(args[3])
                layout.setContentsMargins(args[4], args[5], args[6], args[7])

        return layout

    def _createLabel(self, *args):
        """ Creates a label and customises it.
        This function supports different number of arguments:
        4 args(QWidget, name, Qt, bool)
        """

        label = None

        match len(args):
            case 2:
                label = QtWidgets.QLabel(args[0])
                label.setObjectName(args[1])

            case 3:
                label = QtWidgets.QLabel(args[0])
                label.setObjectName(args[1])
                #check this out (if switch conditions, there is an error)
                if type(args[2] == bool) :
                    label.setHidden(args[2])
                elif type(args[2] == type(QtCore.Qt.AlignCenter)):
                    label.setAlignment(args[2])

            case 4:
                label = QtWidgets.QLabel(args[0])
                label.setObjectName(args[1])
                label.setAlignment(args[2])
                label.setHidden(args[3])

        return label

    def _createButton(self, *args):
        """Creates a button and customises it.
        This function supports different number of arguments:
        4 args(QWidget, name, x, y)
        """

        button = None

        match len(args):
            case 4:
                button = QtWidgets.QPushButton(args[0])
                button.resize(args[2], args[3])
                button.setObjectName(args[1])

        return button

    def _createTextEdit(self, *args):
        """ Creates a text editor and customises it.
        This function supports different number of arguments:
        4 args(QWidget, name, x, y)
        """

        textEdit = None

        match len(args):
            case 4:
                textEdit = QtWidgets.QTextEdit(args[0])
                textEdit.resize(args[2], args[3])
                textEdit.setObjectName(args[1])


        return textEdit

    def _createRadioButton(self, *args):
        """ Creates a radio button and customises it.
        This function supports different number of arguments:
        3 args(QWidget, name, text)
        """

        radioButton = None

        match len(args):
            case 3:
                radioButton = QtWidgets.QRadioButton(args[0])
                radioButton.setObjectName(args[1])
                radioButton.setText(args[2])

        return radioButton

#-----------actions----------------------------------------------

    def _buttonActions(self):
        self.buttonSubmitGoal.clicked.connect(self.submitGoal)

        self.buttonSubmitAch.clicked.connect(self.submitAchievement)

#-----------buttons functions------------------------------------

    def submitGoal(self):
        """ Write info into database and clear textEdit"""
        print("Goal has been recorded")

    def submitAchievement(self):
        """ Write info into database and clear textEdit"""
        print("Achievement has been recorded")


if __name__ == "__main__":
    app = Ui_Application()

    window = Ui_MainWindow()

    window.show()

    app.exec()