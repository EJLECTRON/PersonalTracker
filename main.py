"""
Tasks:
    On going:
            Code:
            - DRY (have to think about using decorators)
            - take an idea of interface from utorrent
            - add dialog windows
            - add colors
            - admit what I have to do next

            Noncode:
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
            - make a window resizeable with flexible interface

            -- search ho to make a better calendar
            -- add logging system (in future with databases)
            -- if I had an empty space, I would add a cyclic video with capybaras

    Done stuff:
            - add a remainder panel on first tab, which states what I planned to do today (25.10.22)
            - refactor names of variables (25.10.22)
            - add date at 1 tab (24.10.22)
            - add local directory to git (24.10.22)
"""


from PyQt5 import QtCore, QtWidgets


class Ui_Application(QtWidgets.QApplication):
    """ Custom class for application"""
    def __init__(self):
        super(Ui_Application, self).__init__([])

        self._setStylesApp()

    def _setStylesApp(self):
        styles = """
            QLabel{
                font-size: 20px;
                color: #3fc46c;
            }
            
            QPushButton {
                color: #3fc46c;
            }
            
            QDateEdit {
                color: #3fc46c;
            }
            
            QTextEdit {
                color: #3fc46c;
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
            
            QWidget {
                background-color: #c46c3f;
            }
        """

        self.setStyleSheet(styles)

class Ui_MainWindow(QtWidgets.QMainWindow):
    """ Custom class for Main Window"""
    def __init__(self):
        """ Initializes  window"""
        super().__init__()

        self._setupUi()


    def _setupUi(self):
        """ Initializes all objects in app"""
        self.x = 200
        self.y = 150
        self.WIDTH = 1400
        self.HEIGHT = 700

        self.setObjectName("self")
        self.setGeometry(self.x, self.y, self.WIDTH, self.HEIGHT)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self._setupTabs()
        self._setupLayouts()
        self._setupLabels()
        self._setupTextEditors()
        self._setupCalenders()
        self._setupButtons()
        self._setupBars()
        self._setupRadioButtons()

        self.setCentralWidget(self.centralwidget)

        self._setupTexts()
        self.tabWidget.setCurrentIndex(0)

    def _setupLabels(self):
        """ Initializes labels and place it in grid"""
        self.shareLabel = self._createLabel(self.tab1gridLayoutW, "shareLabel")

        self.noteLabel = self._createLabel(self.tab1gridLayoutW, "noteLabel", QtCore.Qt.AlignCenter)

        #this text appears only after the achievement has been recorded
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
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, self.WIDTH - 100, self.HEIGHT- 100))
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")

        self.tab_1 = self._createTab("tab_1")

        self.tab_2 = self._createTab("tab_2")

        self.tabWidget.addTab(self.tab_1, "")
        self.tabWidget.addTab(self.tab_2, "")

    def _setupButtons(self):
        self.buttonSubmitAch = QtWidgets.QPushButton(self.tab1gridLayoutW)
        self.buttonSubmitAch.resize(50, 50)
        self.buttonSubmitAch.setObjectName("buttonSubmitAch")

        self.tab1gridLayout.addWidget(self.buttonSubmitAch, 3, 0, 1, 1)

        self.buttonSubmitGoal = QtWidgets.QPushButton(self.tab1gridLayoutW)
        self.buttonSubmitGoal.resize(50, 50)
        self.buttonSubmitGoal.setObjectName("buttonSubmitGoal")

        self.tab1gridLayout.addWidget(self.buttonSubmitGoal, 3, 1, 1, 1)

        self.buttonSearch = QtWidgets.QPushButton(self.tab2gridLayoutW)
        self.buttonSearch.resize(50, 50)
        self.buttonSearch.setObjectName("buttonSearch")

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

    def _setupBars(self):
        """ Initializes bars and place it in grid"""
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, self.WIDTH - 100, self.HEIGHT - 100))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

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
        self.textEditSubmitAch = QtWidgets.QTextEdit(self.tab1gridLayoutW)
        self.textEditSubmitAch.resize(100, 200)
        self.textEditSubmitAch.setObjectName("textEditSubmitAch")


        self.textEditSubmitGoal = QtWidgets.QTextEdit(self.tab1gridLayoutW)
        self.textEditSubmitGoal.resize(100, 200)
        self.textEditSubmitGoal.setObjectName("textEditSubmitGoal")

        self.tab1gridLayout.addWidget(self.textEditSubmitAch, 2, 0, 1, 1)

        self.tab1gridLayout.addWidget(self.textEditSubmitGoal, 2, 1, 1, 1)

        self.textBrowserShow = QtWidgets.QTextBrowser(self.tab2gridLayoutW)
        self.textBrowserShow.resize(200, 100)
        self.textBrowserShow.setObjectName("textBrowserShow")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab2gridLayoutW)
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.tab2gridLayout.addWidget(self.textBrowserShow, 2, 0, 1, 1)

        self.tab2gridLayout.addWidget(self.textBrowser_2, 1, 1, 1, 1)

    def _setupTexts(self):
        """ Sets text of all widgets"""

        _translate = QtCore.QCoreApplication.translate

        self.setWindowTitle(_translate("MainWindow", "PersonalApp"))

        self.shareLabel.setText(_translate("MainWindow", "Share with me your achievement:"))
        self.noteLabel.setText(_translate("MainWindow", "Note: If you want to see your history then move to the next tab"))
        self.setGoalLabel.setText(_translate("MainWindow", "Set your goal for the following day:"))
        self.recordedLabel.setText(_translate("MainWindow", "Achievement has been recorded"))
        self.statLabel.setText(_translate("MainWindow", "There'll be some statistics"))
        self.dateRangeLabel.setText(_translate("MainWindow", "Select date or range of dates to see your history:"))
        self.tasksToDoLabel.setText(_translate("Main Window", "That is your tasks for today:"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

        self.textEditSubmitAch.setText(_translate("MainWindow", "That is first textEdit"))
        self.textEditSubmitGoal.setText(_translate("MainWindow", "That is second textEdit"))

        self.buttonSubmitAch.setText(_translate("MainWindow", "Submit a result"))
        self.buttonSubmitGoal.setText(_translate("MainWindow", "Submit a goal"))
        self.buttonSearch.setText(_translate("MainWindow", "Search"))

    def _setupGroupBoxes(self):
        "Initializes group boxes and add them to the grid"

    def _setupRadioButtons(self):
        """ Initializes radiobuttons for the groupbox"""

        self.radioButton = QtWidgets.QRadioButton(self.tab1gridLayoutW)
        self.radioButton.setText("First task")
        self.radioButton.setObjectName("radioButton")

        self.tab1VBox02.addWidget(self.radioButton)

        self.radioButton_2 = QtWidgets.QRadioButton(self.tab1gridLayoutW)
        self.radioButton_2.setText("Second task")
        self.radioButton_2.setObjectName("radioButton_2")

        self.tab1VBox02.addWidget(self.radioButton_2)

        self.radioButton_3 = QtWidgets.QRadioButton(self.tab1gridLayoutW)
        self.radioButton_3.setText("Third task")
        self.radioButton_3.setObjectName("radioButton_3")

        self.tab1VBox02.addWidget(self.radioButton_3)

    def _createTab(self, name):
        tab = QtWidgets.QWidget()
        tab.setObjectName(name)

        return tab

    def _createLabel(self, *args):
        """ Creates a label and customises it.
        This function supports different number of arguments(next numbers doesn't include 'self'):
        4 args(QWidget, str, Qt, bool)
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


if __name__ == "__main__":
    app = Ui_Application()

    window = Ui_MainWindow()

    window.show()

    app.exec()