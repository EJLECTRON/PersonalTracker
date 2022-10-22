from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        """ Initializes  window"""
        super().__init__()

        self.setupUi()

    def setupUi(self):
        """ Creates all objects in app"""
        self.WIDTH = 1024
        self.HEIGHT = 576

        self.setObjectName("self")
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, self.WIDTH, self.HEIGHT))
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")

        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")

        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, self.WIDTH - 100, self.HEIGHT - 100))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName("textEdit")

        self.gridLayout.addWidget(self.textEdit, 2, 1, 1, 1)

        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.textEdit_2 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_2.setObjectName("textEdit_2")

        self.gridLayout.addWidget(self.textEdit_2, 2, 0, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setHidden(True)

        self.gridLayout.addWidget(self.label_4, 3, 0, 2, 1)

        self.tabWidget.addTab(self.tab_1, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, self.WIDTH - 100, self.HEIGHT - 100))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser.setObjectName("textBrowser")

        self.gridLayout_2.addWidget(self.textBrowser, 1, 0, 1, 1)

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.gridLayout_2.addWidget(self.textBrowser_2, 1, 1, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)

        self.dateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        self.dateEdit.setObjectName("dateEdit")

        self.gridLayout_2.addWidget(self.dateEdit, 0, 2, 1, 1)

        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, self.WIDTH - 100, self.HEIGHT - 100))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Share with me your achievement"))
        self.label_2.setText(_translate("MainWindow", "Note: If you want to see your history then move to the next tab"))

        self.label_5.setText(_translate("MainWindow", "Set your goal for the following day:"))

        self.label_4.setText(_translate("MainWindow", "Achievement has been recorded"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Tab 1"))

        self.label_3.setText(_translate("MainWindow", "Select date:"))
        self.label_6.setText(_translate("MainWindow", "History:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = Ui_MainWindow()

    window.show()

    app.exec()