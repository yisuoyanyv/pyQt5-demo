import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class window(QWidget):
    def __init__(self, parent = None):
        super(window,self).__init__(parent)
        self.resize(500,50)
        self.setWindowTitle("pyQt5")
        self.label = QLabel(self)
        self.label.setText("Hello world oo!")
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.move(50,20)


def main():
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
