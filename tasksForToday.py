import pymongo.errors
from PyQt5 import QtWidgets
from datetime import datetime


from ui_dialog import Ui_Dialog
from functionallity_reportError import ErrorDialog



class TasksForToday(QtWidgets.QDialog):
    def __init__(self, user):
        QtWidgets.QDialog.__init__(self)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.user = user

        self.tasksForToday= self.__extractTasksForDay()

        self.__insertTasksForTodayIntoWindow(self.tasksForToday, currentDate = datetime.now().strftime("%d/%m/%Y"))


    def __insertTasksForTodayIntoWindow(self, collOfTasks, currentDate):
        if self.ui.textBrowser.toPlainText() == "":
            innerCounter = 0

            try:
                for task in collOfTasks[currentDate]:
                    self.ui.textBrowser.append(task[str(innerCounter + 1)])
                    innerCounter += 1
            except KeyError:
                self.ui.textBrowser.append(collOfTasks["error"])

    def __extractTasksForDay(self):
        try:
            db = self.user.client['TestData']
        except pymongo.errors.OperationFailure:
            ErrorDialog()

        currentCollection = db[self.user.userName + "'s tasks"]

        try:
            result = currentCollection.find_one({}, {"_id": 0, datetime.now().strftime("%d/%m/%Y"): 1})
        except KeyError:
            result = {"error": "Tasks for you wasn't found, report this issue"}

        if result == {} or result == None:
            result = {"error": "You don't have tasks for today"}

        return result