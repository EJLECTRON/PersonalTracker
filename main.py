import PySide6.QtWidgets as qtw
import PySide6.QtCore as qtc
import PySide6.QtGui as qtg


class Window(qtw.QWidget):
    """ initializes  window"""
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        """ Initializes fields and places them into QVBoxLayout"""

        self.WIDTH = 1024
        self.HEIGHT = 576

        #styles
        textFont = qtg.QFont("Times", 8, qtg.QFont.Bold)
        stylesheet = """
        Q
        """


        labelInfo = qtw.QLabel("Input an action")
        labelInfo.setFont(textFont)


        inputInfo = qtw.QLineEdit()
        inputInfo.setFixedSize(300, 50)

        #fake input (I'll place here diagram soon)
        plotStatistics = qtw.QTextEdit()
        plotStatistics.setFixedSize(300, 250)

        # fake input (I'll place here history of inputs soon)
        textStatistics = qtw.QTextEdit()
        textStatistics.setFixedSize(300, 250)


        buttonInputInfo = qtw.QPushButton("Submit")
        buttonInputInfo.setFixedSize(100, 50)
        buttonInputInfo.clicked.connect(self.ButtonPressed(inputInfo))


        #layouts
        inputLayout = qtw.QVBoxLayout()
        inputLayout.setSpacing(10)
        inputLayout.addWidget(labelInfo)
        inputLayout.addWidget(inputInfo)
        inputLayout.addWidget(buttonInputInfo)

        displayLayout = qtw.QVBoxLayout()
        displayLayout.setSpacing(30)
        displayLayout.addWidget(plotStatistics)
        displayLayout.addWidget(textStatistics)

        #I need to fill a space with image
        justInCaseLayout = qtw.QVBoxLayout()
        justLayout = qtw.QTextEdit()
        justLayout.setFixedSize(300, 300)
        justInCaseLayout.addWidget(justLayout)
        """widgetJust = qtw.QWidget()
        justInCaseLayout.addWidget(widgetJust)
        widgetJust.setStyleSheet("QWidget#Form {background-image: images\\w.png; background-attachment: fixed}")"""


        #main grid
        grid = qtw.QGridLayout()
        grid.setAlignment(qtc.Qt.AlignCenter)
        grid.setVerticalSpacing(100)
        grid.setHorizontalSpacing(100)

        grid.addLayout(inputLayout, 0, 0)
        grid.addLayout(justInCaseLayout, 1, 0)
        grid.addLayout(displayLayout, 0, 1, 2, 1)

        self.setLayout(grid)
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)

        self.show()


    def ButtonPressed(self, inputInfo):
        print(inputInfo.text())




if __name__ == '__main__':
    app = qtw.QApplication()

    window = Window()

    app.exec()
