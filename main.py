#TODO: sliding leftMenu

# TODO: When you click on calendar: on the first tab you get achievements
#                                   on the second tab you get goals

import webbrowser

from PyQt5 import QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5 import uic

from ui_mainInterface import *
from jsonHandler import *
from ui_dataAnalysisInterface import *

from pymongo import MongoClient
import datetime

class Ui_Application(QtWidgets.QApplication):
    """ Custom class for application"""
    def __init__(self):
        super(Ui_Application, self).__init__([])

        self.__setStylesApp()

    def __setStylesApp(self):
        pass

class User:
    def __init__(self, clientName):
        cfg = ConfigHandler()

        cfg.takeCredentialsFromConfig(clientName)

        self.userName = clientName
        self.client = MongoClient(cfg.gatherCredentials())

    def getTasksForDay(self, date):
        db = self.client['TestData']

        try:
            currentCollection = db['Tasks of ' + self.userName]

            tasks = []

            return currentCollection.find_one({}, {"_id": 0, date: 1})
        except KeyError:
            return ["You don't have tasks for today"]

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, clientName):
        QtWidgets.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        try:
            self.__buttonActions()

            self.__animationActions()
        except Exception:
            raise Exception("Something goes wrong")

        self.user = User(clientName)

        self.dialogTasks = QtWidgets.QDialog()
        uic.loadUi('ui/dialog_tasks.ui', self.dialogTasks)
#-----------actions----------------------------------------------

    def __buttonActions(self):

        self.ui.mainCentralBtn.clicked.connect(self.__submitGoal)

        self.ui.mainBottomBtn.clicked.connect(self.__submitAchievement)

        self.ui.archiveBtn.clicked.connect(self.__showArchive)

        self.__leftMenuActions()

        self.__socialNetworkActions()

    def __leftMenuActions(self):
        self.ui.getTasksBtn.clicked.connect(self.__showTasks)

        self.ui.homeBtn.clicked.connect(self.__showHome)

        self.ui.archiveBtn.clicked.connect(self.__showArchive)

        self.ui.dataAnalysisBtn.clicked.connect(self.__showAnalysis)

        self.ui.articlesBtn.clicked.connect(self.__showArticles)

        self.ui.settingsBtn.clicked.connect(self.__showSettings)

        self.ui.reportBtn.clicked.connect(self.__showReport)

    def __socialNetworkActions(self):
        self.ui.youtubeBtn.clicked.connect(self.__redirectToYoutube)

        self.ui.twitterBtn.clicked.connect(self.__redirectToTwitter)

        self.ui.githubBtn.clicked.connect(self.__redirectToGitHub)

        self.ui.linkedinBtn.clicked.connect(self.__redirectToLinked)

        self.ui.instagramBtn.clicked.connect(self.__redirectToInstagram)

        self.ui.stackoverflowBtn.clicked.connect(self.__redirectToStackOverFlow)

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

    #TODO: remake this function, it's looks awful
    def __showTasks(self):
        currentDate = '15/1/2023'

        listOfTasks = self.user.getTasksForDay(currentDate)

        innerCounter = 0
        try:
            self.dialogTasks.textBrowser.append(listOfTasks[0])
        except KeyError:
            for task in listOfTasks['15/1/2023']:
                self.dialogTasks.textBrowser.append(task[str(innerCounter + 1)])
                innerCounter += 1

        self.dialogTasks.show()

    def __showHome(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def __showArchive(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def __showAnalysis(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def __showArticles(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def __showSettings(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def __showReport(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def __redirectToYoutube(self):
        webbrowser.open('https://www.youtube.com/')

    def __redirectToTwitter(self):
        webbrowser.open('https://twitter.com/home')

    def __redirectToGitHub(self):
        webbrowser.open('https://github.com/EJLECTRON?tab=repositories')

    def __redirectToLinked(self):
        webbrowser.open('https://www.linkedin.com/in/mykola-ishchenko-53a65b249/')

    def __redirectToInstagram(self):
        webbrowser.open('https://www.instagram.com/')

    def __redirectToStackOverFlow(self):
        webbrowser.open('https://stackoverflow.com/')

if __name__ == "__main__":
    """
    print(db_collection.find_one()['task1'])

    client.close()
    """
    app = Ui_Application()

    mainWindow = MainWindow('Nick')

    mainWindow.show()

    app.exec()


