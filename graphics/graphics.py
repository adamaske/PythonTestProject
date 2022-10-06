import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *

class Graphics():
    def __init__(self):
        print("Setup Graphics!")
        #Create window
        app = QApplication(sys.argv)
        self.win = Window()
        self.win.show()
        self.ShowImage('/hammer.png')
        app.exec_()
    def ShowImage(self, name):
        print("Show image!")
        self.win.showImage(name)


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Python")
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)  

    def showImage(self, path):
        pixmap = QPixmap(path)
        print(path)
        self.label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())  
        self.show()  

if __name__ == '__main__':
    #When run from this file
    import constants as c
    import helpers as h
    g = Graphics()
else:
    import graphics.constants as c
    import graphics.helpers as h

