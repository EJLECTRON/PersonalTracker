from main_view import Ui_Application
from ui_new_main_interface import Ui_PersonalTracker

from PyQt5.QtWidgets import QMainWindow, QWidget, QCheckBox, QPushButton, QTextEdit, QHBoxLayout, QVBoxLayout, QFrame, QSizePolicy, QSpacerItem, QSpinBox, QLabel
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

        main_text_edit, needed_checkbox, delete_button, emoji_button, edit_button, submit_button, \
            evaluation_of_task, evaluation_of_task_label = CustomWidgetsForTasks.create_custom_widgets(number_of_task)

        needed_layout, top_layout, top_inner_layout, bottom_layout \
            = CustomWidgetsForTasks.create_custom_layouts(number_of_task)

        needed_widget, top_widget, top_inner_widget, bottom_widget \
            = CustomWidgetsForTasks.create_custom_qwidgets(number_of_task)

        for item in [edit_button, submit_button, emoji_button, delete_button, needed_checkbox]:
            top_inner_layout.addWidget(item)

        top_inner_widget.setLayout(top_inner_layout)

        top_layout.addWidget(main_text_edit)
        top_layout.addItem(QSpacerItem(50, 25, QSizePolicy.Minimum, QSizePolicy.Expanding))
        top_layout.addWidget(top_inner_widget)
        top_widget.setLayout(top_layout)

        bottom_layout.addWidget(evaluation_of_task_label)
        bottom_layout.addWidget(evaluation_of_task)
        bottom_widget.setLayout(bottom_layout)

        needed_layout.addWidget(top_widget)
        needed_layout.addWidget(bottom_widget)

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
        main_text_edit = QTextEdit()
        main_text_edit.setObjectName(f"number{number_of_task}TaskLineEdit")
        main_text_edit.setPlaceholderText("Enter your task here \n (max 105 symbols)")
        main_text_edit.setReadOnly(True)
        main_text_edit.setFrameStyle(QFrame.NoFrame)
        main_text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        main_text_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        main_text_edit.setMinimumSize(80, 60)
        main_text_edit.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)

        return main_text_edit

    @staticmethod
    def create_custom_widgets(number_of_task: int):
        """
        Creates custom widgets for tasks
        :number_of_task: int
        :return: (QTextEdit, QCheckBox, QPushButton, QPushButton, QPushButton, QPushButton)
        """

        main_text_edit = CustomWidgetsForTasks.create_custom_text_edit(number_of_task)

        evaluation_of_task = QSpinBox()
        evaluation_of_task.setObjectName(f"number{number_of_task}TaskEvalution")
        evaluation_of_task.setFixedSize(50, 20)
        evaluation_of_task.setRange(0, 200)
        evaluation_of_task.setSingleStep(10)
        evaluation_of_task.setButtonSymbols(2)

        evaluation_of_task_label = QLabel()
        evaluation_of_task_label.setText("Evaluation of the task in karma points:")

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
            partial(CustomWidgetsForTasks.change_statements_of_elements, [emoji_button, edit_button, submit_button, main_text_edit]))

        submit_button.clicked.connect(
            partial(CustomWidgetsForTasks.change_statements_of_elements, [emoji_button, edit_button, submit_button, main_text_edit]))

        emoji_button.clicked.connect(partial(CustomWidgetsForTasks.emoji_button_action, main_text_edit))

        return main_text_edit, needed_checkbox, delete_button, emoji_button, edit_button, submit_button, evaluation_of_task, evaluation_of_task_label

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

        top_layout = QHBoxLayout()
        top_layout.setObjectName(f"number{number_of_task}TaskTopLayout")
        top_layout.setContentsMargins(0, 0, 0, 0)

        top_inner_layout = QHBoxLayout()
        top_inner_layout.setObjectName(f"number{number_of_task}TaskTopInnerLayout")
        top_inner_layout.setContentsMargins(0, 0, 0, 0)

        bottom_layout = QHBoxLayout()
        bottom_layout.setObjectName(f"number{number_of_task}TaskBottomLayout")
        bottom_layout.setContentsMargins(0, 0, 0, 0)
        bottom_layout.setAlignment(Qt.AlignLeft)

        needed_layout = QVBoxLayout()
        needed_layout.setObjectName(f"number{number_of_task}TaskLayout")
        needed_layout.setContentsMargins(5, 10, 5, 10)

        return needed_layout, top_layout, top_inner_layout, bottom_layout

    @staticmethod
    def create_custom_qwidgets(number_of_task: int):
        """
        Creates custom qwidgets for tasks
        :number_of_task: int
        :return: (QWidget, QWidget, QWidget)
        """
        top_widget = QWidget()
        top_widget.setObjectName(f"number{number_of_task}TaskTopWidget")

        top_inner_widget = QWidget()
        top_inner_widget.setObjectName(f"number{number_of_task}TaskTopInnerWidget")

        bottom_widget = QWidget()
        bottom_widget.setObjectName(f"number{number_of_task}TaskBottomWidget")

        needed_widget = QWidget()
        needed_widget.setObjectName(f"number{number_of_task}TaskWidget")
        needed_widget.setFixedSize(300, 100)

        return needed_widget, top_widget, top_inner_widget, bottom_widget

if __name__ == "__main__":
    app = Ui_Application()

    test_window = UIIII()
    test_window.show()

    app.exec()

