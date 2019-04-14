from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QVBoxLayout, QGridLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "Scheduler"
        self.left = 500
        self.top = 200
        self.width = 400
        self.height = 100
        self.iconName = "home.png"


        self.InitWindow()
#---------------------------------------------making buttons and control on geometry--------------------------------# 
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon (QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateLayout()
        vbox = QVBoxLayout()
        vbox.addWidget (self.groupBox)
        
        self.btn = QPushButton("FCFS")
        self.btn.setFont(QtGui.QFont("Sanserif", 15))
        self.btn.clicked.connect(self.FCFS)
        vbox.addWidget(self.btn)

        self.setLayout(vbox)
        
        self.btn = QPushButton("SJF")
        self.btn.setFont(QtGui.QFont("Sanserif", 15))
        self.btn.clicked.connect(self.SJF)
        vbox.addWidget(self.btn)

        self.setLayout(vbox)

        self.btn = QPushButton("PRIORITY")
        self.btn.setFont(QtGui.QFont("Sanserif", 15))
        self.btn.clicked.connect(self.PRIORITY)
        vbox.addWidget(self.btn)

        self.setLayout(vbox)

        self.btn = QPushButton("ROUND_ROBIN")
        self.btn.setFont(QtGui.QFont("Sanserif", 15))
        self.btn.clicked.connect(self.ROUND_ROBIN)
        vbox.addWidget(self.btn)

        self.setLayout(vbox)

        self.show()
#---------------------------------------making box to write words-------------------------------------#
    def CreateLayout(self):
        self.groupBox = QGroupBox("what scheduler do you want ?")
        gridLayout = QGridLayout()

       # button = QPushButton("FCFS", self)
        #button.setIcon(QtGui.QIcon("FCFS.png"))
        #button.setIconSize(QtCore.QSize(40,40))
        #button.setMinimumHeight(40)
        #gridLayout.addWidget(button, 0,0)
        #button.clicked.connect(self.FCFS)

        #button1 = QPushButton("SJF", self)
        #button1.setIcon(QtGui.QIcon("SJF.png"))
        #button1.setIconSize(QtCore.QSize(40,40))
        #button1.setMinimumHeight(40)
       # gridLayout.addWidget(button1, 0,1)


        #button2 = QPushButton("PRIORITY", self)
        #button2.setIcon(QtGui.QIcon("PRIORITY.png"))
       # button2.setIconSize(QtCore.QSize(40,40))
      #  button2.setMinimumHeight(40)
     #   gridLayout.addWidget(button2, 1,0)


#        button3 = QPushButton("ROUND ROBIN", self)
 #       button3.setIcon(QtGui.QIcon("ROUND ROBIN.png"))
  #      button3.setIconSize(QtCore.QSize(40,40))
   #     button3.setMinimumHeight(40)
    #    gridLayout.addWidget(button3, 1,1)

        self.groupBox.setLayout(gridLayout)
#----------------------------------------making windows of each type----------------------------------------#

    def FCFS(self):
        FCFS = QDialog()
        FCFS.setModal(True)
        FCFS.exec()

    def SJF(self):
        SJF = QDialog()
        SJF.setModal(True)
        SJF.exec()

    def ROUND_ROBIN(self):
        ROUND_ROBIN = QDialog()
        ROUND_ROBIN.setModal(True)
        ROUND_ROBIN.exec()

    def PRIORITY(self):
        PRIORITY= QDialog()
        PRIORITY.setModal(True)
        PRIORITY.exec()
#-------------------------------------------------------main-----------------------------------------------------------#
if __name__=="__main__":
    App = QApplication(sys.argv)
    window = window()
    sys.exit(App.exec())
