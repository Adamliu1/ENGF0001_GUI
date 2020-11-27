from main_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication

import sys
import main_serial

class myWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()

        #initial timer for auto refresh



        self.temp = 0
        #print(self.dragPos)

        # Links
        self.overview_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.overview_page))
        self.heating_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.heating_page))
        #self.overview_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.overview_page))
        
        #Custom quit button
        self.quit_btn.clicked.connect(lambda : sys.exit())

        def moveWindow(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                #print(self.dragPos)
                event.accept()
        # App events
        def mousePressEvent(event):
            self.dragPos = event.globalPos()

        self.MainFrame.mousePressEvent = mousePressEvent
        self.MainFrame.mouseMoveEvent = moveWindow

    def getData(self):
        self.temp = main_serial.getdata()
        #convert to degree celcius
        self.temp = float(self.temp)
        temp_degree = round(self.temp - 273.15, 1)

        self.Temperature_Value.setText(" " + str(temp_degree))
        self.label_17.setText(str(self.temp))  
        self.Temperature_Value.adjustSize()
        #QApplication.processEvents()

                             
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    main_window = myWindow()
    # REMOVE TITLE BAR
    main_window.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    main_window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    
    timer = QtCore.QTimer()
    timer.timeout.connect(main_window.getData)
    timer.start(1000)   

    main_window.show()
    sys.exit(app.exec_())


