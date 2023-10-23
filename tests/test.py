from main_view import Ui_Application
from ui_new_main_interface import Ui_PersonalTracker

from PyQt5.QtWidgets import QMainWindow, QWidget, QCheckBox, QPushButton, QTextEdit, QHBoxLayout, QVBoxLayout, QFrame, QSizePolicy, QSpacerItem
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
        """
        Creates new task widget and adds it to scroll area
        """
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

        needed_text_edit = CustomWidgetsForTasks.create_custom_text_edit(number_of_task)

        needed_checkbox = QCheckBox()
        needed_checkbox.setObjectName(f"number{number_of_task}TaskCheckBox")

        delete_button = QPushButton()
        delete_button.setObjectName(f"number{number_of_task}DeleteButton")
        delete_button.setText("Delete task")
        delete_button.setFixedSize(75, 20)

        emoji_button = QPushButton()
        emoji_button.setObjectName(f"number{number_of_task}EmojiButton")
        emoji_button.setText("\U0001F600")
        emoji_button.setFixedSize(20, 20)

        additional_layout = QVBoxLayout()
        additional_layout.setObjectName(f"number{number_of_task}TaskAdditionalLayout")
        additional_layout.setContentsMargins(0, 0, 0, 0)
        additional_inner_layout = QHBoxLayout()
        additional_inner_layout.setObjectName(f"number{number_of_task}TaskAdditionalInnerLayout")
        additional_inner_layout.setContentsMargins(0, 0, 0, 0)


        additional_widget = QWidget()
        additional_widget.setObjectName(f"number{number_of_task}TaskAdditionalWidget")
        additional_inner_widget = QWidget()
        additional_inner_widget.setObjectName(f"number{number_of_task}TaskAdditionalInnerWidget")

        additional_inner_layout.addWidget(emoji_button)
        additional_inner_layout.addWidget(needed_checkbox)
        additional_inner_layout.addWidget(delete_button)
        additional_inner_widget.setLayout(additional_inner_layout)

        additional_layout.addWidget(additional_inner_widget)
        additional_layout.addItem(QSpacerItem(100, 100, QSizePolicy.Minimum, QSizePolicy.Expanding))
        additional_widget.setLayout(additional_layout)

        needed_layout = QHBoxLayout()
        needed_layout.setObjectName(f"number{number_of_task}TaskLayout")
        needed_layout.setContentsMargins(5, 10, 5, 0)

        needed_layout.addWidget(needed_text_edit)
        needed_layout.addWidget(additional_widget)

        needed_widget = QWidget()

        needed_widget.setObjectName(f"number{number_of_task}TaskWidget")
        needed_widget.setFixedSize(300, 75)
        needed_widget.setLayout(needed_layout)
        needed_widget.layout().setAlignment(Qt.AlignTop)

        self.number_of_current_tasks += 1
        return needed_widget

    def close_window(self):
        """ close window"""
        self.close()

    def hide_window(self):
        self.showMinimized()

class CustomWidgetsForTasks:

    @staticmethod
    def create_custom_text_edit(number_of_task: int):
        """
        Creates custom text edit widget
        :number_of_task: int
        :return: QTextEdit
        """
        needed_text_edit = QTextEdit()
        needed_text_edit.setObjectName(f"number{number_of_task}TaskLineEdit")
        needed_text_edit.setPlaceholderText("Enter your task here \n (max 105 symbols)")
        needed_text_edit.setFrameStyle(QFrame.NoFrame)
        needed_text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        needed_text_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        needed_text_edit.setMinimumSize(100, 60)
        needed_text_edit.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)

        return needed_text_edit



if __name__ == "__main__":
    app = Ui_Application()

    test_window = UIIII()
    test_window.show()

    app.exec()

