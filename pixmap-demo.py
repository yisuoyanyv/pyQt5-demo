import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    l1 = QLabel()
    l1.setPixmap(QPixmap("pyQt5-demo\python-logo.png"))

    vbox = QVBoxLayout()
    vbox.addWidget(l1)
    win.setLayout(vbox)
    win.setWindowTitle("Qpixmap Demo")
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()
