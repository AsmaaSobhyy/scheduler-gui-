import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

num=1
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
    i, okPressed = QInputDialog.getInt(self, "Get integer","number of processes:",1, 0, 100, 1)
    if okPressed:
        return(i)

#-----------------------priority----------------------------------#
def priority(self):
    process = []
    final=[]
    for j in range (0,num):
        arr, okPressed = QInputDialog.getInt(self, "Get integer",f"process {j} arrive time:",0, 0, 100, 1)
        burst, okPressed = QInputDialog.getInt(self, "Get integer",f"process {j} burst timt:",0, 0, 100, 1)
        prior, okPressed = QInputDialog.getInt(self, "Get integer",f"process {j} priority:",0, 0, 100, 1)
        process.append({'arr':arr,'burst':burst,'prior':prior})
    sortedProcess = sorted(process, key=lambda k: k['arr'])
    start=0
    current = 0
    k=0
    f=0
    imp = sortedProcess[0]
    for m in range (0,num):
        for n in range(0,num):
            if (sortedProcess[m]['arr'] <= current) and (sortedProcess[n]['arr']<=current) :    
                if sortedProcess[m]['prior'] < sortedProcess[n]['prior']:
                    #final.append(sortedProcess[m])
                    imp = sortedProcess[m]
                    k=m
                    #current = current + sortedProcess[m]['burst']
                    
                    
                else:
                    imp = sortedProcess[n]
                    k=n
                    #final.append(sortedProcess[m])
                    #current = current + sortedProcess[n]['burst']
            else :
                    imp = sortedProcess[m]     
        final.append(imp)
        final[f]['number']=k
        f=f+1
        current=current +imp['burst']
        #del sortedProcess[k]
    print(final)        
    for g in range(0,num): 
        k=final[g]['number']      
        button = QPushButton(f'process{k}', w)
        button.move(start,10)
        x=5*sortedProcess[g]['burst']
        button.resize(100,20)
        start= start+100
        button.show()       

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
                priority(w)

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

