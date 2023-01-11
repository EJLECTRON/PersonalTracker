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
from PyQt5.QtCore import QEvent

from ui_interface import *
from jsonHandler import *

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

        self.__buttonActions()

        self.show()

#-----------actions----------------------------------------------

    def __buttonActions(self):

        self.ui.mainCentralBtn.clicked.connect(self.submitGoal)

        self.ui.mainBottomBtn.clicked.connect(self.submitAchievement)


#-----------buttons functions------------------------------------

    def submitGoal(self):
        """ Write info into database and clear textEdit"""
        print("Goal has been recorded")

    def submitAchievement(self):
        """ Write info into database and clear textEdit"""
        print("Achievement has been recorded")


if __name__ == "__main__":
    cfg = ConfigHandler()

    cfg.takeCredentialsFromConfig('admin')

    client = MongoClient(cfg.gatherCredentials())

    db = client['TestData']

    db_collection = db['testData']

    print(db_collection.find_one())

    client.close()
"""
    app = Ui_Application()
    
        window = MainWindow()
    
        window.show()
    
        app.exec()
"""

