from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Mywindows(QMainWindow):
    def __init__(self):
        super(Mywindows, self).__init__()
        self.setGeometry(200,200,600,600)
        self.setWindowTitle("CSEEE 23 - Bioreactor Client GUI")
        self.initUI()

    def initUI(self):

        self.label = QtWidgets.QLabel(self)
        self.label.setText("My first label")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Set")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()


def winodws():
    app = QApplication(sys.argv)
    win = Mywindows()

    win.show()
    sys.exit(app.exec_())

winodws()