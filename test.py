import sys
import PySide6.QtWidgets as qtw
import PySide6.QtGui as qtg

class Window(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        Button1 = qtw.QPushButton('Up')
        Button2 = qtw.QPushButton('Left')
        Button3 = qtw.QPushButton('Right')
        Button4 = qtw.QPushButton('Down')

        grid = qtw.QGridLayout()
        grid.addWidget(Button1, 0, 1)
        grid.addWidget(Button2, 1, 0)
        grid.addWidget(Button3, 1, 2)
        grid.addWidget(Button4, 1, 1)

        self.setLayout(grid)
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('PyQt6 Grid Layout')
        self.show()

if __name__ == "__main__":
    app = qtw.QApplication()

    window = Window()

    app.exec()