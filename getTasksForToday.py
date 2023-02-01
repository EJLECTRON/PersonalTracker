import pymongo.errors
from PyQt5 import QtWidgets
from datetime import datetime


from ui_dialog import Ui_Dialog
from differentWindows import ErrorDialog


class TasksForToday(QtWidgets.QDialog):
    def __init__(self, user):
        QtWidgets.QDialog.__init__(self)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.user = user

        self.tasksForToday= self.__extractTasksForDay()

        self.__insertTasksForTodayIntoWindow(self.tasksForToday, currentDate = datetime.now().strftime("%d/%m/%Y"))

    #TODO: add an error handling to that
    def __insertTasksForTodayIntoWindow(self, collOfTasks, currentDate):
        if self.ui.textBrowser.toPlainText() == "":
            print(collOfTasks[currentDate][0])

            for id, task in collOfTasks[currentDate][0].items():
                self.ui.textBrowser.append(task)


    # TODO: add an error handling to that
    def __extractTasksForDay(self):
        try:
            db = self.user.client['TestData']
        except pymongo.errors.OperationFailure:
            pass

        currentCollection = db[self.user.userName + "'s tasks"]

        try:
            result = currentCollection.find_one({}, {"_id": 0, datetime.now().strftime("%d/%m/%Y"): 1})
        except KeyError:
            result = {"error": "Tasks for you wasn't found, report this issue"}

        if result == {} or result == None:
            result = {"error": "You don't have tasks for today"}

        return result