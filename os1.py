import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


#-------------------------------------initializing window-----------------#
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('scheduler')       
    
        self.show()
#---------------------------popUp that gets the type--------------------#
def getType(self):
    items = ("FCFS","SJF Preemptive","SJF Non Preemptive","Priority Preemptive","Priority Non Preemptive","round robin")
    item, okPressed = QInputDialog.getItem(self, "Get item","scheduler type:", items, 0, False)
    if okPressed and item:
        return(item)

#-------------------------------gets the number of processes---------------------------------#

def numberOfProcess(self):
    i, okPressed = QInputDialog.getInt(self, "Get integer","number of processes:",0, 0, 100, 1)
    if okPressed:
        return(i)

#------------------------type button------------------------------#
#@pyqtSlot()
def ontype(self):
        typ = getType(w)
        if typ == 'FCFS':
                print("fcfs function here")

        elif typ == 'SJF Preemptive':
                print("SJF preemptive function here")

        elif typ == 'SJF Non Preemptive':
                print("SJF Non Preemptive fn here")

        elif typ == 'Priority Preemptive':
                print("Priority Preemptive fn here")

        elif typ == 'Priority Non Preemptive':
                print("Priority Non Preemptive fn here")

        elif typ == 'round robin':
                print("round robin fn here")
        

#----------------------------count button--------------------------------------#
#@pyqtSlot()
def oncount(self):
        num = numberOfProcess(w)
        return num

#------------------------------main-------------------#

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    w =  Example()

    typeButton = QPushButton('type button', w)
    typeButton.move(100,70)
    typeButton.clicked.connect(ontype)
    typeButton.show()

    
    sys.exit(app.exec_())

