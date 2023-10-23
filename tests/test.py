from main_view import Ui_Application
from ui_new_main_interface import Ui_PersonalTracker

from PyQt5.QtWidgets import QMainWindow, QWidget, QCheckBox, QPushButton, QTextEdit, QHBoxLayout, QVBoxLayout, QFrame, QSizePolicy, QSpacerItem
from PyQt5.QtCore import QPoint, Qt
from PyQt5 import QtGui

from functools import partial

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

        needed_text_edit, needed_checkbox, delete_button, emoji_button, edit_button, submit_button = CustomWidgetsForTasks.create_custom_widgets(number_of_task)

        additional_layout, additional_inner_layout, needed_layout = CustomWidgetsForTasks.create_custom_layouts(number_of_task)

        additional_widget, additional_inner_widget, needed_widget = CustomWidgetsForTasks.create_custom_qwidgets(number_of_task)

        for item in [edit_button, submit_button, emoji_button, delete_button, needed_checkbox]:
            additional_inner_layout.addWidget(item)

        additional_inner_widget.setLayout(additional_inner_layout)

        additional_layout.addWidget(additional_inner_widget)
        additional_layout.addItem(QSpacerItem(100, 100, QSizePolicy.Minimum, QSizePolicy.Expanding))
        additional_widget.setLayout(additional_layout)

        needed_layout.addWidget(needed_text_edit)
        needed_layout.addWidget(additional_widget)

        needed_widget.setLayout(needed_layout)

        self.number_of_current_tasks += 1
        return needed_widget

    def close_window(self):
        """ close window"""
        self.close()

    def hide_window(self):
        self.showMinimized()

    def edit_button(self, number_of_task: int):
        pass



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
        needed_text_edit.setReadOnly(True)
        needed_text_edit.setFrameStyle(QFrame.NoFrame)
        needed_text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        needed_text_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        needed_text_edit.setMinimumSize(100, 60)
        needed_text_edit.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)

        return needed_text_edit

    @staticmethod
    def create_custom_widgets(number_of_task: int):
        """
        Creates custom widgets for tasks
        :number_of_task: int
        :return: (QTextEdit, QCheckBox, QPushButton, QPushButton, QPushButton, QPushButton)
        """

        needed_text_edit = CustomWidgetsForTasks.create_custom_text_edit(number_of_task)

        needed_checkbox = QCheckBox()
        needed_checkbox.setObjectName(f"number{number_of_task}TaskCheckBox")

        delete_button = QPushButton()
        delete_button.setObjectName(f"number{number_of_task}DeleteButton")
        delete_button.setText("\U0001F5D1")
        delete_button.setFixedSize(20, 20)

        emoji_button = QPushButton()
        emoji_button.setObjectName(f"number{number_of_task}EmojiButton")
        emoji_button.setText("\U0001F600")
        emoji_button.setFixedSize(20, 20)
        emoji_button.setHidden(True)

        edit_button = QPushButton()
        edit_button.setObjectName(f"number{number_of_task}EditButton")
        edit_button.setText("\U0001F4DD")
        edit_button.setFixedSize(20, 20)

        submit_button = QPushButton()
        submit_button.setObjectName(f"number{number_of_task}SubmitButton")
        submit_button.setText("\U00002714")
        submit_button.setFixedSize(20, 20)
        submit_button.setHidden(True)

        edit_button.clicked.connect(
            partial(CustomWidgetsForTasks.change_statements_of_elements, [emoji_button, edit_button, submit_button, needed_text_edit]))

        submit_button.clicked.connect(
            partial(CustomWidgetsForTasks.change_statements_of_elements, [emoji_button, edit_button, submit_button, needed_text_edit]))

        emoji_button.clicked.connect(partial(CustomWidgetsForTasks.emoji_button_action, needed_text_edit))

        return needed_text_edit, needed_checkbox, delete_button, emoji_button, edit_button, submit_button

    @staticmethod
    def change_statements_of_elements(list_of_elements: list):
        CustomWidgetsForTasks.change_hidden_statement_of_buttons_to_opposite(list_of_elements[:len(list_of_elements) - 1])
        CustomWidgetsForTasks.change_read_only_statement_to_opposite(list_of_elements[-1])

    @staticmethod
    def change_hidden_statement_of_buttons_to_opposite(list_of_buttons: list):
        for item in list_of_buttons:
            item.setHidden(not item.isHidden())

    @staticmethod
    def change_read_only_statement_to_opposite(text_edit: QTextEdit):
        text_edit.setReadOnly(not text_edit.isReadOnly())

    @staticmethod
    def emoji_button_action(text_edit: QTextEdit):
        text_edit.insertPlainText("\U0001F600")



    @staticmethod
    def create_custom_layouts(number_of_task: int):
        """
        Creates custom layouts for tasks
        :number_of_task: int
        :return: (QVBoxLayout, QHBoxLayout, QHBoxLayout)
        """

        additional_layout = QVBoxLayout()
        additional_layout.setObjectName(f"number{number_of_task}TaskAdditionalLayout")
        additional_layout.setContentsMargins(0, 0, 0, 0)

        additional_inner_layout = QHBoxLayout()
        additional_inner_layout.setObjectName(f"number{number_of_task}TaskAdditionalInnerLayout")
        additional_inner_layout.setContentsMargins(0, 0, 0, 0)

        needed_layout = QHBoxLayout()
        needed_layout.setObjectName(f"number{number_of_task}TaskLayout")
        needed_layout.setContentsMargins(5, 10, 5, 0)

        return additional_layout, additional_inner_layout, needed_layout

    @staticmethod
    def create_custom_qwidgets(number_of_task: int):
        """
        Creates custom qwidgets for tasks
        :number_of_task: int
        :return: (QWidget, QWidget, QWidget)
        """
        additional_widget = QWidget()
        additional_widget.setObjectName(f"number{number_of_task}TaskAdditionalWidget")

        additional_inner_widget = QWidget()
        additional_inner_widget.setObjectName(f"number{number_of_task}TaskAdditionalInnerWidget")

        needed_widget = QWidget()
        needed_widget.setObjectName(f"number{number_of_task}TaskWidget")
        needed_widget.setFixedSize(300, 75)

        return additional_widget, additional_inner_widget, needed_widget

if __name__ == "__main__":
    app = Ui_Application()

    test_window = UIIII()
    test_window.show()

    app.exec()

