#TODO: sliding leftMenu

import webbrowser

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QMovie
from datetime import datetime

from ui_mainInterface import *
from ui_data_analysis_interface import *
from different_windows import MessageAlert
from user_class import User
from tasks_class import TasksForDay
from error_class import ErrorIntoUI
from quote_class import Quote

class Ui_Application(QtWidgets.QApplication):
    """ Custom class for application"""
    def __init__(self):
        super(Ui_Application, self).__init__([])

        self.__set_styles_app()

    def __set_styles_app(self):
        pass

class MainWindow(QtWidgets.QMainWindow):
    """ Custom class for main window"""
    def __init__(self, user: User):
        """ creating window and setting up all actions"""
        QtWidgets.QMainWindow.__init__(self)

        #params of window between reloading
        self.setWindowTitle("PersonalTracker")
        self.resize(1000, 614)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.ui = Ui_PersonalTracker()
        self.ui.setupUi(self)

        self.user = user

        try:
            self.__button_actions()

            self.__animation_actions()

            self.__today_tasks_actions()

        except Exception as error:
            print(error)
#-----------actions----------------------------------------------

    def __button_actions(self):
        """ setting up all actions for buttons"""
        self.ui.getQuoteBtn.clicked.connect(self.__get_quote)

        self.__left_menu_actions()

        self.__social_network_actions()

        self.__date_edit_actions()

    def __left_menu_actions(self):
        """ setting up all actions for left menu bar"""
        self.ui.homeBtn.clicked.connect(self.__show_home)

        self.ui.makePublicationBtn.clicked.connect(self.__show_publication)

        self.ui.archiveBtn.clicked.connect(self.__show_archive)

        self.ui.dataAnalysisBtn.clicked.connect(self.__show_analysis)

        self.ui.articlesBtn.clicked.connect(self.__show_articles)

        self.ui.settingsBtn.clicked.connect(self.__show_settings)

        self.ui.reportBtn.clicked.connect(self.__show_report)

    def __social_network_actions(self):
        """ setting up all actions for social network buttons"""
        self.ui.youtubeBtn.clicked.connect(self.__redirect_to_youtube)

        self.ui.twitterBtn.clicked.connect(self.__redirect_to_twitter)

        self.ui.githubBtn.clicked.connect(self.__redirect_to_github)

        self.ui.linkedinBtn.clicked.connect(self.__redirect_to_linked)

        self.ui.instagramBtn.clicked.connect(self.__redirect_to_instagram)

        self.ui.stackoverflowBtn.clicked.connect(self.__redirect_to_stackoverflow)

    def __today_tasks_actions(self):
        """ gets all tasks for today and shows them for current user in home page"""
        tasks_for_today= TasksForDay()

        tasks_tuple = tasks_for_today.get_tasks_for_given_date(self.user, datetime.now().strftime("%d/%m/%Y"))

        if tasks_tuple:
            self.ui.homeTasksTextBrowser.clear()

            for task in tasks_tuple:
                self.ui.homeTasksTextBrowser.append(str(task))


    def __animation_actions(self):
        """ setting up all actions for animation"""
        self.__capybara_animation()

    def __date_edit_actions(self):
        """ setting up *fill* to current date"""
        pass

#-----------animation functions----------------------------------q
    def __capybara_animation(self):
        """ setting up capybara animation"""
        self.gif = QtGui.QMovie("images/sleeping_capybara.gif")

        self.ui.capybara_2.setMovie(self.gif)

        self.gif.start()

#-----------buttons functions------------------------------------

    def __submit_goal(self):
        """ Write info into database and clears goalLineEdit(line for tasks)"""
        data_needed_to_submit = self.ui.goalLineEdit.text()
        date_needed_to_submit = self.ui.goalDateEdit.date().toString("dd/MM/yyyy")

        if not data_needed_to_submit == "":
            response = self.user.submit_goal(data_needed_to_submit, date_needed_to_submit)

            self.ui.goalLineEdit.setText("")

            if date_needed_to_submit == datetime.now().strftime("%d/%m/%Y"):
                self.__today_tasks_actions()

            if response:
                self.__show_alert_message(response)

    def __submit_achievement(self):
        """ Write info into database and clear textEdit(line for achievements)"""
        data_needed_to_submit = self.ui.achLineEdit.text()
        date_needed_to_submit = datetime.now().strftime("%d/%m/%Y")

        if not data_needed_to_submit == "":
            response = self.user.submit_achievement(data_needed_to_submit, date_needed_to_submit)

            self.ui.achLineEdit.setText("")
            
            if response:
                self.__show_alert_message(response)

    def __get_quote(self):
        """ Write quote into popping window"""
        quote = Quote().get_quote(self.user)

        self.alert_message = MessageAlert(quote)

        self.alert_message.show()

    def __show_home(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def __show_publication(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def __show_archive(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def __show_analysis(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def __show_articles(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def __show_settings(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def __show_report(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    #TODO: if right click on social media button then show window to edit link
    def __redirect_to_youtube(self):
        webbrowser.open('https://www.youtube.com/')

    def __redirect_to_twitter(self):
        webbrowser.open('https://twitter.com/home')

    def __redirect_to_github(self):
        webbrowser.open('https://github.com/EJLECTRON?tab=repositories')

    def __redirect_to_linked(self):
        webbrowser.open('https://www.linkedin.com/in/mykola-ishchenko-53a65b249/')

    def __redirect_to_instagram(self):
        webbrowser.open('https://www.instagram.com/')

    def __redirect_to_stackoverflow(self):
        webbrowser.open('https://stackoverflow.com/')

    def __show_alert_message(self, response: str):
        """
        Shows alert message
        :param response: shows response from server
        :return: None
        """
        self.alert_message = MessageAlert(response)

        self.alert_message.show()



