# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 614)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("*\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QTextBrowser\n"
"{\n"
"    background-color: #FFFFFF;\n"
"}\n"
"\n"
"#centralwidget\n"
"{\n"
"    background-color: #FBEEC1;\n"
"}\n"
"\n"
"#leftMenuContainer\n"
"{\n"
"    background-color: #DCDEDF;\n"
"}\n"
"\n"
"#leftSubContainer QPushButton\n"
"{\n"
"    text-align: left;\n"
"    padding: 5px 10px;\n"
"    border-top-left-radius: 10 px;\n"
"    border-bottom-left-radius: 10 px;\n"
"}\n"
"\n"
"#quoteTextBrow\n"
"{\n"
"    background-color: #B4DFE5;\n"
"}\n"
"\n"
"#mainSubContainer QPushButton\n"
"{\n"
"    border: 1px solid;\n"
"    border-radius: 3px;\n"
"    text-align: left;\n"
"}\n"
"\n"
"#mainSubContainer QPushButton:hover\n"
"{\n"
"    background-color: #F4976C;\n"
"}\n"
"\n"
"#leftMenuContainer QPushButton:hover\n"
"{\n"
"    background-color: #BDBBBB;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMenuContainer = QtWidgets.QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName("leftMenuContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.leftSubContainer = QtWidgets.QWidget(self.leftMenuContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftSubContainer.sizePolicy().hasHeightForWidth())
        self.leftSubContainer.setSizePolicy(sizePolicy)
        self.leftSubContainer.setObjectName("leftSubContainer")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.leftSubContainer)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.leftTopFrame = QtWidgets.QFrame(self.leftSubContainer)
        self.leftTopFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftTopFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftTopFrame.setObjectName("leftTopFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.leftTopFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menuBtn = QtWidgets.QPushButton(self.leftTopFrame)
        self.menuBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/6498732_application_list_menu_mobile_smartphone_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QtCore.QSize(24, 24))
        self.menuBtn.setObjectName("menuBtn")
        self.horizontalLayout_2.addWidget(self.menuBtn)
        self.verticalLayout_4.addWidget(self.leftTopFrame, 0, QtCore.Qt.AlignTop)
        self.leftCentralFrame = QtWidgets.QFrame(self.leftSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftCentralFrame.sizePolicy().hasHeightForWidth())
        self.leftCentralFrame.setSizePolicy(sizePolicy)
        self.leftCentralFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftCentralFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftCentralFrame.setObjectName("leftCentralFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftCentralFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.homeBtn = QtWidgets.QPushButton(self.leftCentralFrame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-home-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QtCore.QSize(24, 24))
        self.homeBtn.setObjectName("homeBtn")
        self.verticalLayout_2.addWidget(self.homeBtn)
        self.archiveBtn = QtWidgets.QPushButton(self.leftCentralFrame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-news-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.archiveBtn.setIcon(icon2)
        self.archiveBtn.setIconSize(QtCore.QSize(24, 24))
        self.archiveBtn.setObjectName("archiveBtn")
        self.verticalLayout_2.addWidget(self.archiveBtn)
        self.dataAnalysisBtn = QtWidgets.QPushButton(self.leftCentralFrame)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/7549001_user_interface_graph_chart_business_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dataAnalysisBtn.setIcon(icon3)
        self.dataAnalysisBtn.setIconSize(QtCore.QSize(24, 24))
        self.dataAnalysisBtn.setObjectName("dataAnalysisBtn")
        self.verticalLayout_2.addWidget(self.dataAnalysisBtn)
        self.articlesBtn = QtWidgets.QPushButton(self.leftCentralFrame)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-news-64 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.articlesBtn.setIcon(icon4)
        self.articlesBtn.setIconSize(QtCore.QSize(24, 24))
        self.articlesBtn.setObjectName("articlesBtn")
        self.verticalLayout_2.addWidget(self.articlesBtn)
        self.verticalLayout_4.addWidget(self.leftCentralFrame, 0, QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.leftBottomFrame = QtWidgets.QFrame(self.leftSubContainer)
        self.leftBottomFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftBottomFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftBottomFrame.setObjectName("leftBottomFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.leftBottomFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.settingsBtn = QtWidgets.QPushButton(self.leftBottomFrame)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-settings-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsBtn.setIcon(icon5)
        self.settingsBtn.setIconSize(QtCore.QSize(24, 24))
        self.settingsBtn.setObjectName("settingsBtn")
        self.verticalLayout_3.addWidget(self.settingsBtn)
        self.reportBtn = QtWidgets.QPushButton(self.leftBottomFrame)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/7324045_ui_interface_email_mail_message_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reportBtn.setIcon(icon6)
        self.reportBtn.setIconSize(QtCore.QSize(24, 24))
        self.reportBtn.setObjectName("reportBtn")
        self.verticalLayout_3.addWidget(self.reportBtn)
        self.verticalLayout_4.addWidget(self.leftBottomFrame, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.leftSubContainer, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.leftMenuContainer)
        self.rightMenuContainer = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightMenuContainer.sizePolicy().hasHeightForWidth())
        self.rightMenuContainer.setSizePolicy(sizePolicy)
        self.rightMenuContainer.setObjectName("rightMenuContainer")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.stackedWidget = QtWidgets.QStackedWidget(self.rightMenuContainer)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setObjectName("stackedWidget")
        self.mainMenu = QtWidgets.QWidget()
        self.mainMenu.setObjectName("mainMenu")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.mainMenu)
        self.verticalLayout_14.setContentsMargins(0, 0, 5, 5)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.mainSubContainer = QtWidgets.QWidget(self.mainMenu)
        self.mainSubContainer.setObjectName("mainSubContainer")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.mainSubContainer)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 11)
        self.verticalLayout_5.setSpacing(11)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.mainTopWidget = QtWidgets.QWidget(self.mainSubContainer)
        self.mainTopWidget.setObjectName("mainTopWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.mainTopWidget)
        self.horizontalLayout_6.setContentsMargins(6, 5, 11, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.leftSubWidget = QtWidgets.QWidget(self.mainTopWidget)
        self.leftSubWidget.setObjectName("leftSubWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.leftSubWidget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.mainTopFrame = QtWidgets.QFrame(self.leftSubWidget)
        self.mainTopFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainTopFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainTopFrame.setObjectName("mainTopFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.mainTopFrame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tasksLabel = QtWidgets.QLabel(self.mainTopFrame)
        self.tasksLabel.setObjectName("tasksLabel")
        self.horizontalLayout_4.addWidget(self.tasksLabel)
        self.verticalLayout_9.addWidget(self.mainTopFrame)
        self.getTasksBtn = QtWidgets.QPushButton(self.leftSubWidget)
        self.getTasksBtn.setMinimumSize(QtCore.QSize(85, 0))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/get.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getTasksBtn.setIcon(icon7)
        self.getTasksBtn.setIconSize(QtCore.QSize(24, 24))
        self.getTasksBtn.setObjectName("getTasksBtn")
        self.verticalLayout_9.addWidget(self.getTasksBtn, 0, QtCore.Qt.AlignHCenter)
        self.capybara = QtWidgets.QFrame(self.leftSubWidget)
        self.capybara.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.capybara.setFrameShadow(QtWidgets.QFrame.Raised)
        self.capybara.setObjectName("capybara")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.capybara)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.capybara_2 = QtWidgets.QLabel(self.capybara)
        self.capybara_2.setText("")
        self.capybara_2.setPixmap(QtGui.QPixmap(":/images/images/Знімок екрана 2023-01-08 142920.png"))
        self.capybara_2.setObjectName("capybara_2")
        self.horizontalLayout_7.addWidget(self.capybara_2)
        self.verticalLayout_9.addWidget(self.capybara)
        self.horizontalLayout_6.addWidget(self.leftSubWidget)
        self.centralSubWidget = QtWidgets.QWidget(self.mainTopWidget)
        self.centralSubWidget.setObjectName("centralSubWidget")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.centralSubWidget)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.quoteFrame = QtWidgets.QFrame(self.centralSubWidget)
        self.quoteFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.quoteFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.quoteFrame.setObjectName("quoteFrame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.quoteFrame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.quoteLabel = QtWidgets.QLabel(self.quoteFrame)
        self.quoteLabel.setObjectName("quoteLabel")
        self.horizontalLayout_8.addWidget(self.quoteLabel)
        self.verticalLayout_12.addWidget(self.quoteFrame)
        self.quoteTextBrow = QtWidgets.QTextBrowser(self.centralSubWidget)
        self.quoteTextBrow.setObjectName("quoteTextBrow")
        self.verticalLayout_12.addWidget(self.quoteTextBrow)
        self.horizontalLayout_6.addWidget(self.centralSubWidget)
        self.rigthSubWidget = QtWidgets.QWidget(self.mainTopWidget)
        self.rigthSubWidget.setObjectName("rigthSubWidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.rigthSubWidget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.accFrame = QtWidgets.QFrame(self.rigthSubWidget)
        self.accFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.accFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.accFrame.setObjectName("accFrame")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.accFrame)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.accLabel = QtWidgets.QLabel(self.accFrame)
        self.accLabel.setObjectName("accLabel")
        self.verticalLayout_11.addWidget(self.accLabel, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_10.addWidget(self.accFrame)
        self.youtubeBtn = QtWidgets.QPushButton(self.rigthSubWidget)
        self.youtubeBtn.setMinimumSize(QtCore.QSize(81, 0))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-youtube-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.youtubeBtn.setIcon(icon8)
        self.youtubeBtn.setIconSize(QtCore.QSize(24, 24))
        self.youtubeBtn.setObjectName("youtubeBtn")
        self.verticalLayout_10.addWidget(self.youtubeBtn, 0, QtCore.Qt.AlignHCenter)
        self.twitterBtn = QtWidgets.QPushButton(self.rigthSubWidget)
        self.twitterBtn.setMinimumSize(QtCore.QSize(76, 0))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-twitter-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.twitterBtn.setIcon(icon9)
        self.twitterBtn.setIconSize(QtCore.QSize(24, 24))
        self.twitterBtn.setObjectName("twitterBtn")
        self.verticalLayout_10.addWidget(self.twitterBtn, 0, QtCore.Qt.AlignHCenter)
        self.githubBtn = QtWidgets.QPushButton(self.rigthSubWidget)
        self.githubBtn.setMinimumSize(QtCore.QSize(72, 0))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-github-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.githubBtn.setIcon(icon10)
        self.githubBtn.setIconSize(QtCore.QSize(24, 24))
        self.githubBtn.setObjectName("githubBtn")
        self.verticalLayout_10.addWidget(self.githubBtn, 0, QtCore.Qt.AlignHCenter)
        self.linkedinBtn = QtWidgets.QPushButton(self.rigthSubWidget)
        self.linkedinBtn.setMinimumSize(QtCore.QSize(82, 0))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-linkedin-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.linkedinBtn.setIcon(icon11)
        self.linkedinBtn.setIconSize(QtCore.QSize(24, 24))
        self.linkedinBtn.setObjectName("linkedinBtn")
        self.verticalLayout_10.addWidget(self.linkedinBtn, 0, QtCore.Qt.AlignHCenter)
        self.instagramBtn = QtWidgets.QPushButton(self.rigthSubWidget)
        self.instagramBtn.setMinimumSize(QtCore.QSize(93, 0))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-instagram-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.instagramBtn.setIcon(icon12)
        self.instagramBtn.setIconSize(QtCore.QSize(24, 24))
        self.instagramBtn.setObjectName("instagramBtn")
        self.verticalLayout_10.addWidget(self.instagramBtn, 0, QtCore.Qt.AlignHCenter)
        self.stackoverflowBtn = QtWidgets.QPushButton(self.rigthSubWidget)
        self.stackoverflowBtn.setMinimumSize(QtCore.QSize(120, 0))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-stack-overflow-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stackoverflowBtn.setIcon(icon13)
        self.stackoverflowBtn.setIconSize(QtCore.QSize(24, 24))
        self.stackoverflowBtn.setObjectName("stackoverflowBtn")
        self.verticalLayout_10.addWidget(self.stackoverflowBtn, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem1)
        self.horizontalLayout_6.addWidget(self.rigthSubWidget, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_5.addWidget(self.mainTopWidget)
        self.mainCentralWidget = QtWidgets.QWidget(self.mainSubContainer)
        self.mainCentralWidget.setObjectName("mainCentralWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.mainCentralWidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.mainCentralFrame = QtWidgets.QFrame(self.mainCentralWidget)
        self.mainCentralFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainCentralFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainCentralFrame.setObjectName("mainCentralFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.mainCentralFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.goalLabel = QtWidgets.QLabel(self.mainCentralFrame)
        self.goalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.goalLabel.setObjectName("goalLabel")
        self.horizontalLayout_3.addWidget(self.goalLabel, 0, QtCore.Qt.AlignRight)
        self.dateEdit = QtWidgets.QDateEdit(self.mainCentralFrame)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_3.addWidget(self.dateEdit, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_7.addWidget(self.mainCentralFrame)
        self.goalLineEdit = QtWidgets.QLineEdit(self.mainCentralWidget)
        self.goalLineEdit.setObjectName("goalLineEdit")
        self.verticalLayout_7.addWidget(self.goalLineEdit)
        self.mainCentralBtn = QtWidgets.QPushButton(self.mainCentralWidget)
        self.mainCentralBtn.setMinimumSize(QtCore.QSize(75, 0))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/icons/sumbit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainCentralBtn.setIcon(icon14)
        self.mainCentralBtn.setIconSize(QtCore.QSize(24, 24))
        self.mainCentralBtn.setObjectName("mainCentralBtn")
        self.verticalLayout_7.addWidget(self.mainCentralBtn, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addWidget(self.mainCentralWidget, 0, QtCore.Qt.AlignBottom)
        self.mainBottomWidget = QtWidgets.QWidget(self.mainSubContainer)
        self.mainBottomWidget.setObjectName("mainBottomWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.mainBottomWidget)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.mainBottomFrame = QtWidgets.QFrame(self.mainBottomWidget)
        self.mainBottomFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainBottomFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainBottomFrame.setObjectName("mainBottomFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.mainBottomFrame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.achLabel = QtWidgets.QLabel(self.mainBottomFrame)
        self.achLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.achLabel.setObjectName("achLabel")
        self.horizontalLayout_5.addWidget(self.achLabel)
        self.verticalLayout_6.addWidget(self.mainBottomFrame)
        self.achLineEdit = QtWidgets.QLineEdit(self.mainBottomWidget)
        self.achLineEdit.setObjectName("achLineEdit")
        self.verticalLayout_6.addWidget(self.achLineEdit)
        self.mainBottomBtn = QtWidgets.QPushButton(self.mainBottomWidget)
        self.mainBottomBtn.setMinimumSize(QtCore.QSize(75, 0))
        self.mainBottomBtn.setIcon(icon14)
        self.mainBottomBtn.setIconSize(QtCore.QSize(24, 24))
        self.mainBottomBtn.setObjectName("mainBottomBtn")
        self.verticalLayout_6.addWidget(self.mainBottomBtn, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addWidget(self.mainBottomWidget)
        self.verticalLayout_14.addWidget(self.mainSubContainer)
        self.stackedWidget.addWidget(self.mainMenu)
        self.archiveMenu = QtWidgets.QWidget()
        self.archiveMenu.setObjectName("archiveMenu")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.archiveMenu)
        self.verticalLayout_15.setContentsMargins(0, 0, 5, 5)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.archiveSubContainer = QtWidgets.QWidget(self.archiveMenu)
        self.archiveSubContainer.setObjectName("archiveSubContainer")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.archiveSubContainer)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.archiveBottomWidget = QtWidgets.QWidget(self.archiveSubContainer)
        self.archiveBottomWidget.setObjectName("archiveBottomWidget")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.archiveBottomWidget)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.subTopWidget = QtWidgets.QWidget(self.archiveBottomWidget)
        self.subTopWidget.setObjectName("subTopWidget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.subTopWidget)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.tasksLabel_2 = QtWidgets.QLabel(self.subTopWidget)
        self.tasksLabel_2.setObjectName("tasksLabel_2")
        self.horizontalLayout_9.addWidget(self.tasksLabel_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.achLabel_2 = QtWidgets.QLabel(self.subTopWidget)
        self.achLabel_2.setObjectName("achLabel_2")
        self.horizontalLayout_9.addWidget(self.achLabel_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_16.addWidget(self.subTopWidget)
        self.subBottomWidget = QtWidgets.QWidget(self.archiveBottomWidget)
        self.subBottomWidget.setObjectName("subBottomWidget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.subBottomWidget)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.tasksTextBrowser = QtWidgets.QTextBrowser(self.subBottomWidget)
        self.tasksTextBrowser.setObjectName("tasksTextBrowser")
        self.horizontalLayout_10.addWidget(self.tasksTextBrowser)
        self.achTextBrowser = QtWidgets.QTextBrowser(self.subBottomWidget)
        self.achTextBrowser.setObjectName("achTextBrowser")
        self.horizontalLayout_10.addWidget(self.achTextBrowser)
        self.verticalLayout_16.addWidget(self.subBottomWidget)
        self.subBottomWidget.raise_()
        self.subTopWidget.raise_()
        self.verticalLayout_18.addWidget(self.archiveBottomWidget)
        self.achiveTopWidget = QtWidgets.QWidget(self.archiveSubContainer)
        self.achiveTopWidget.setObjectName("achiveTopWidget")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.achiveTopWidget)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.achiveTopWidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_17.addWidget(self.calendarWidget)
        self.verticalLayout_18.addWidget(self.achiveTopWidget, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_15.addWidget(self.archiveSubContainer)
        self.stackedWidget.addWidget(self.archiveMenu)
        self.analysisMenu = QtWidgets.QWidget()
        self.analysisMenu.setObjectName("analysisMenu")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.analysisMenu)
        self.verticalLayout_21.setContentsMargins(0, 0, 5, 5)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.analysisSubContainer = QtWidgets.QWidget(self.analysisMenu)
        self.analysisSubContainer.setObjectName("analysisSubContainer")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.analysisSubContainer)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.analysisTopWidget = QtWidgets.QWidget(self.analysisSubContainer)
        self.analysisTopWidget.setObjectName("analysisTopWidget")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.analysisTopWidget)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.plotLabel = QtWidgets.QLabel(self.analysisTopWidget)
        self.plotLabel.setObjectName("plotLabel")
        self.verticalLayout_20.addWidget(self.plotLabel, 0, QtCore.Qt.AlignHCenter)
        self.textBrowser = QtWidgets.QTextBrowser(self.analysisTopWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_20.addWidget(self.textBrowser)
        self.verticalLayout_19.addWidget(self.analysisTopWidget, 0, QtCore.Qt.AlignTop)
        self.analysisBottomWidget = QtWidgets.QWidget(self.analysisSubContainer)
        self.analysisBottomWidget.setObjectName("analysisBottomWidget")
        self.verticalLayout_19.addWidget(self.analysisBottomWidget)
        self.verticalLayout_21.addWidget(self.analysisSubContainer)
        self.stackedWidget.addWidget(self.analysisMenu)
        self.articlesMenu = QtWidgets.QWidget()
        self.articlesMenu.setObjectName("articlesMenu")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.articlesMenu)
        self.verticalLayout_25.setContentsMargins(0, 0, 5, 5)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.articlesSubContainer = QtWidgets.QWidget(self.articlesMenu)
        self.articlesSubContainer.setObjectName("articlesSubContainer")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.articlesSubContainer)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.articlesTopWidget = QtWidgets.QWidget(self.articlesSubContainer)
        self.articlesTopWidget.setObjectName("articlesTopWidget")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.articlesTopWidget)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label = QtWidgets.QLabel(self.articlesTopWidget)
        self.label.setObjectName("label")
        self.verticalLayout_23.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_22.addWidget(self.articlesTopWidget, 0, QtCore.Qt.AlignTop)
        self.articlesBottomWidget = QtWidgets.QWidget(self.articlesSubContainer)
        self.articlesBottomWidget.setObjectName("articlesBottomWidget")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.articlesBottomWidget)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.articlesBottomWidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_24.addWidget(self.textBrowser_2)
        self.verticalLayout_22.addWidget(self.articlesBottomWidget)
        self.verticalLayout_25.addWidget(self.articlesSubContainer)
        self.stackedWidget.addWidget(self.articlesMenu)
        self.settingsMenu = QtWidgets.QWidget()
        self.settingsMenu.setObjectName("settingsMenu")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.settingsMenu)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.settingsSubContainer = QtWidgets.QWidget(self.settingsMenu)
        self.settingsSubContainer.setObjectName("settingsSubContainer")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.settingsSubContainer)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.label_2 = QtWidgets.QLabel(self.settingsSubContainer)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_27.addWidget(self.label_2)
        self.verticalLayout_26.addWidget(self.settingsSubContainer, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.settingsMenu)
        self.reportMenu = QtWidgets.QWidget()
        self.reportMenu.setObjectName("reportMenu")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.reportMenu)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.settingsSubContainer_2 = QtWidgets.QWidget(self.reportMenu)
        self.settingsSubContainer_2.setObjectName("settingsSubContainer_2")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.settingsSubContainer_2)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.label_3 = QtWidgets.QLabel(self.settingsSubContainer_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_28.addWidget(self.label_3)
        self.verticalLayout_29.addWidget(self.settingsSubContainer_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.reportMenu)
        self.verticalLayout_13.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.rightMenuContainer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuBtn.setToolTip(_translate("MainWindow", "Menu"))
        self.homeBtn.setToolTip(_translate("MainWindow", "Home"))
        self.homeBtn.setText(_translate("MainWindow", "Home"))
        self.archiveBtn.setToolTip(_translate("MainWindow", "Archive"))
        self.archiveBtn.setText(_translate("MainWindow", "Archive data"))
        self.dataAnalysisBtn.setToolTip(_translate("MainWindow", "Data Analysis"))
        self.dataAnalysisBtn.setText(_translate("MainWindow", "Data Analysis"))
        self.articlesBtn.setText(_translate("MainWindow", "Helpful articles"))
        self.settingsBtn.setToolTip(_translate("MainWindow", "Settings"))
        self.settingsBtn.setText(_translate("MainWindow", "Settings"))
        self.reportBtn.setToolTip(_translate("MainWindow", "Report"))
        self.reportBtn.setText(_translate("MainWindow", "Report"))
        self.tasksLabel.setText(_translate("MainWindow", "Click on button to discover your tasks for today:"))
        self.getTasksBtn.setText(_translate("MainWindow", "Click Me"))
        self.quoteLabel.setText(_translate("MainWindow", "Quote of a day:"))
        self.accLabel.setText(_translate("MainWindow", "Check out your accounts:"))
        self.youtubeBtn.setText(_translate("MainWindow", "Youtube"))
        self.twitterBtn.setText(_translate("MainWindow", "Twitter"))
        self.githubBtn.setText(_translate("MainWindow", "GitHub"))
        self.linkedinBtn.setText(_translate("MainWindow", "LinkedIn"))
        self.instagramBtn.setText(_translate("MainWindow", "Instagram"))
        self.stackoverflowBtn.setText(_translate("MainWindow", "StackOverFlow"))
        self.goalLabel.setText(_translate("MainWindow", "Set your goal for the chosen day:"))
        self.mainCentralBtn.setText(_translate("MainWindow", "Submit"))
        self.achLabel.setText(_translate("MainWindow", "Share with me your achievement:"))
        self.mainBottomBtn.setText(_translate("MainWindow", "Submit"))
        self.tasksLabel_2.setText(_translate("MainWindow", "Tasks:"))
        self.achLabel_2.setText(_translate("MainWindow", "Achievements:"))
        self.plotLabel.setText(_translate("MainWindow", "There\'ll be plot"))
        self.label.setText(_translate("MainWindow", "Helpful articles:"))
        self.label_2.setText(_translate("MainWindow", "Coming soon...."))
        self.label_3.setText(_translate("MainWindow", "Coming soon...."))
import main_resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
