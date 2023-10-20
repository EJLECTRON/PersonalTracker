from main_view import Ui_Application
from ui_new_main_interface import Ui_PersonalTracker

from PyQt5.QtWidgets import QMainWindow, QWidget, QCheckBox, QPushButton, QTextEdit, QHBoxLayout, QFrame, QSizePolicy
from PyQt5.QtCore import QPoint, Qt
from PyQt5 import QtGui

class UIIII(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_PersonalTracker()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.setupUi(self)
        self.old_pos = self.pos()
        self.number_of_current_tasks = 1

        self.__capybara_animation()
        self.__button_actions()

    def mousePressEvent(self, event):
        """ mouse press event that updates old position of window"""
        self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        """ mouse move event that moves window"""
        delta = QPoint(event.globalPos() - self.old_pos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_pos = event.globalPos()

    def closeEvent(self, event: QtGui.QCloseEvent):
        """ close event that shows message box"""
        event.accept()

    def __capybara_animation(self):
        """ setting up capybara animation"""
        self.gif = QtGui.QMovie("../images/capybara-walk.gif")

        self.ui.capybaraAnimationLabel.setMovie(self.gif)

        self.gif.start()

    def __button_actions(self):
        self.ui.closeWindowBtn.clicked.connect(self.close_window)
        self.ui.collapseWindowBtn.clicked.connect(self.hide_window)
        self.ui.newTaskBtn.clicked.connect(self.create_new_task)


    #-----------actions----------------------------------------------
    def create_new_task(self):
        if self.number_of_current_tasks == 1:
            self.ui.number1TaskWidget.deleteLater()
            self.ui.tasksScrollAreaWidget.layout().setAlignment(Qt.AlignTop)

        new_task_widget = self.create_new_task_widget(self.number_of_current_tasks)
        self.ui.tasksScrollAreaWidget.layout().addWidget(new_task_widget)



    def create_new_task_widget(self, number_of_task: int):
        """
        Creates new task widget
        :number_of_task: int
        :return: QWidget
        """

        needed_layout = QHBoxLayout()
        needed_layout.setObjectName(f"number{number_of_task}TaskLayout")
        needed_layout.setAlignment(Qt.AlignTop)

        needed_text_edit = QTextEdit()
        needed_text_edit.setObjectName(f"number{number_of_task}TaskLineEdit")
        needed_text_edit.setPlaceholderText("Enter your task here")
        #needed_text_edit.setFrameStyle(QFrame.NoFrame)
        needed_text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        needed_text_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        needed_text_edit.setMinimumSize(100, 60)
        needed_text_edit.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)

        needed_checkbox = QCheckBox()
        needed_checkbox.setObjectName(f"number{number_of_task}TaskCheckBox")

        delete_button = QPushButton()
        delete_button.setObjectName(f"number{number_of_task}DeleteButton")
        delete_button.setText("Delete task")
        delete_button.setFixedSize(75, 20)

        needed_layout.addWidget(needed_text_edit)
        needed_layout.addWidget(needed_checkbox)
        needed_layout.addWidget(delete_button)

        needed_widget = QWidget()
        needed_widget.setObjectName(f"number{number_of_task}TaskWidget")
        needed_widget.setLayout(needed_layout)

        self.number_of_current_tasks += 1
        return needed_widget

    def close_window(self):
        """ close window"""
        self.close()

    def hide_window(self):
        self.showMinimized()

if __name__ == "__main__":
    app = Ui_Application()

    test_window = UIIII()
    test_window.show()

    app.exec()

