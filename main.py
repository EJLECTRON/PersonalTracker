#TODO: sliding leftMenu

# TODO: When you click on calendar: on the first tab you get achievements
#                                   on the second tab you get goals

import webbrowser

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QMovie
from datetime import datetime

from ui_mainInterface import *
from ui_dataAnalysisInterface import *
from differentWindows import ErrorDialog, MessageAlert
from userClass import User
from getTasksForToday import TasksForToday

from pymongo import MongoClient

class Ui_Application(QtWidgets.QApplication):
    """ Custom class for application"""
    def __init__(self):
        super(Ui_Application, self).__init__([])

        self.__setStylesApp()

    def __setStylesApp(self):
        pass

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, clientName):
        QtWidgets.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.user = User(clientName)

        try:
            self.__buttonActions()

            self.__animationActions()

            self.__todayTasksActions()
        except Exception:
            raise Exception("Something goes wrong")
#-----------actions----------------------------------------------

    def __buttonActions(self):

        self.ui.mainCentralBtn.clicked.connect(self.__submitGoal)

        self.ui.mainBottomBtn.clicked.connect(self.__submitAchievement)

        self.ui.archiveBtn.clicked.connect(self.__showArchive)

        self.__leftMenuActions()

        self.__socialNetworkActions()

        self.__dateEditActions()

    def __leftMenuActions(self):
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

    def __todayTasksActions(self):
        self.todayTasksWindow = TasksForToday(self.user)

        self.ui.getTasksBtn.clicked.connect(self.todayTasksWindow.show)

    def __animationActions(self):
        self.__capybaraAnimation()

    def __dateEditActions(self):
        currentDate = QDate.fromString(datetime.now().strftime("%d/%m/%Y"), "dd/MM/yyyy")

        self.ui.goalDateEdit.setDate(currentDate)

#-----------animation functions----------------------------------q
    def __capybaraAnimation(self):

        self.gif = QtGui.QMovie("images/sleeping_capybara.gif")
        #self.gif = QtGui.QMovie("images/capybara.gif")

        self.ui.capybara_2.setMovie(self.gif)

        self.gif.start()

#-----------buttons functions------------------------------------

    def __submitGoal(self):
        """ Write info into database and clear textEdit"""
        dataNeededToSubmit = self.ui.goalLineEdit.text()
        dateNeededToSubmit = self.ui.goalDateEdit.date().toString("dd/MM/yyyy")

        if not dataNeededToSubmit == "":
            # TODO: implement functionallity
            self.user.submitGoal(dataNeededToSubmit, dateNeededToSubmit)

        self.ui.goalLineEdit.setText("")

        self.__showAlertMessage()

    def __submitAchievement(self):
        """ Write info into database and clear textEdit"""
        dataNeededToSubmit = self.ui.achLineEdit.text()
        dateNeededToSubmit = datetime.now().strftime("%d/%m/%Y")

        if not dataNeededToSubmit == "":
            # TODO: implement functionallity
            self.user.submitAch(dataNeededToSubmit, dateNeededToSubmit)

        self.ui.goalLineEdit.setText("")

        self.__showAlertMessage()

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

    def __showAlertMessage(self):
        self.alertMessage = MessageAlert("Data has been recorded")

        self.alertMessage.show()

if __name__ == "__main__":
    app = Ui_Application()

    mainWindow = MainWindow('Nick')

    mainWindow.show()

    app.exec()


