import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from priority import *

num=1
#-------------------------------------initializing window-----------------#
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('scheduler')       
    
        self.show()

 
#---------------------------popUp that gets the type--------------------#
def getType(self):
    items = ("FCFS","SJF Preemptive","SJF Non Preemptive","Priority Preemptive","Priority Non Preemptive","round robin")
    item, okPressed = QInputDialog.getItem(self, "Get item","scheduler type:", items, 0, False)
    if okPressed and item:
        return(item)
#------------------------------------------------------------------------------
#-------------------------------gets the number of processes---------------------------------#

def numberOfProcess(self):
    i, okPressed = QInputDialog.getInt(self, "Get integer","number of processes:",1, 0, 100, 1)
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
                priority(w,True,num)

        elif typ == 'Priority Non Preemptive':
                print("Priority Non Preemptive fn here")
                priority(w,False,num)

        elif typ == 'round robin':
                print("round robin fn here")
        

#----------------------------count button--------------------------------------#
#@pyqtSlot()
def oncount(self):
        global num 
        num = numberOfProcess(w)
        return num

#------------------------------main-------------------#

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    w =  Example()

    typeButton = QPushButton('type button', w)
    countButton = QPushButton('count button', w)
    typeButton.move(100,70)
    countButton.move(100,90)
    typeButton.clicked.connect(ontype)
    countButton.clicked.connect(oncount)
    typeButton.show()
    countButton.show()
    

    
    sys.exit(app.exec_())

