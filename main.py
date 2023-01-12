# TODO: When you click on calendar: on the first tab you get achievements
#                                   on the second tab you get goals

from PyQt5 import QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5 import uic

from ui_interface import *
from jsonHandler import *
from dialog_tasks import *

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

        #self.dialog =

        try:
            self.__buttonActions()

            self.__animationActions()
        except Exception:
            raise Exception("Something goes wrong")

        self.show()

#-----------actions----------------------------------------------

    def __buttonActions(self):

        self.ui.mainCentralBtn.clicked.connect(self.__submitGoal)

        self.ui.mainBottomBtn.clicked.connect(self.__submitAchievement)

        self.ui.getTasksBtn.clicked.connect(self.__showTasks)

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
        pass

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
    
    window = MainWindow()
    
    window.show()

    app.exec()


