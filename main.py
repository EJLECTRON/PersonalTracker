# TODO: When you click on calendar: on the first tab you get achievements
#                                   on the second tab you get goals

from PyQt5 import QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5 import uic

from ui_mainInterface import *
from jsonHandler import *
from dialog_tasks import *
from ui_archiveInterface import *
from ui_articlesInterface import *
from ui_dataAnalysisInterface import *

from pymongo import MongoClient

class Ui_Application(QtWidgets.QApplication):
    """ Custom class for application"""
    def __init__(self):
        super(Ui_Application, self).__init__([])

        self.__setStylesApp()

    def __setStylesApp(self):
        pass

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        try:
            self.__buttonActions()

            self.__animationActions()
        except Exception:
            raise Exception("Something goes wrong")

        self.dialogTasks = QtWidgets.QDialog()
        uic.loadUi('ui/dialog_tasks.ui', self.dialogTasks)
#-----------actions----------------------------------------------

    def __buttonActions(self):

        self.ui.mainCentralBtn.clicked.connect(self.__submitGoal)

        self.ui.mainBottomBtn.clicked.connect(self.__submitAchievement)

        self.leftMenuActions()

    #TODO: Make it open to other windows, perhaps put it in separate class
    def leftMenuActions(self):
        self.ui.getTasksBtn.clicked.connect(self.__showTasks)

        self.ui.homeBtn.clicked.connect(self.showHome)

        self.ui.archiveBtn.clicked.connect(self.showArchive)

        self.ui.dataAnalysisBtn.clicked.connect(self.showAnalysis)

        self.ui.articlesBtn.clicked.connect(self.showArticles)

    def __animationActions(self):
        self.__capybaraAnimation()

#-----------animation functions----------------------------------q
    def __capybaraAnimation(self):
        self.gif = QtGui.QMovie("images/sleeping_capybara.gif")
        #self.gif = QtGui.QMovie("images/capybara.gif")

        self.ui.capybara_2.setMovie(self.gif)

        self.gif.start()

#-----------buttons functions------------------------------------

    def __submitGoal(self):
        """ Write info into database and clear textEdit"""
        print("Goal has been recorded")

    def __submitAchievement(self):
        """ Write info into database and clear textEdit"""
        print("Achievement has been recorded")

    def __showTasks(self):
        self.dialogTasks.show()

    #TODO: fix the issue: i change "screen" only once (figure out about currectIndex())
    def showHome(self):
        stackedWindows.setCurrentIndex(0)
        print(stackedWindows.currentIndex())

    def showArchive(self):
        stackedWindows.setCurrentIndex(1)
        print(stackedWindows.currentIndex())

    def showAnalysis(self):
        stackedWindows.setCurrentIndex(2)
        print(stackedWindows.currentIndex())

    def showArticles(self):
        stackedWindows.setCurrentIndex(3)
        print(stackedWindows.currentIndex())

if __name__ == "__main__":
    """
    cfg = ConfigHandler()

    cfg.takeCredentialsFromConfig('admin')

    client = MongoClient(cfg.gatherCredentials())

    db = client['TestData']

    db_collection = db['testData']

    print(db_collection.find_one()['task1'])

    client.close()
    """
    app = Ui_Application()

    stackedWindows = QtWidgets.QStackedWidget()

    mainWindow = MainWindow()

    archiveWindow = QtWidgets.QWidget()
    Ui_ArchiveWidget().setupUi(archiveWindow)

    analysisWindow = QtWidgets.QWidget()
    Ui_DataAnalysisWidget().setupUi(analysisWindow)

    articlesWindow = QtWidgets.QWidget()
    Ui_ArticlesWidget().setupUi(articlesWindow)

    stackedWindows.addWidget(mainWindow)
    stackedWindows.addWidget(archiveWindow)
    stackedWindows.addWidget(analysisWindow)
    stackedWindows.addWidget(articlesWindow)

    stackedWindows.show()
    app.exec()


