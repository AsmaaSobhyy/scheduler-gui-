import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def getType(self):
    items = ("FCFS","SJF","Priority","round robin")
    item, okPressed = QInputDialog.getItem(self, "Get item","scheduler type:", items, 0, False)
    if okPressed and item:
        return(item)

def numberOfProcess(self):
    i, okPressed = QInputDialog.getInt(self, "Get integer","number of processes:",0, 0, 100, 1)
    if okPressed:
        return(i)

#@pyqtSlot()
def onClick(self):
   # schedulerType = getType(self)
    print('PyQt5 button click')


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500, 500)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    #schedulerType = getType(w)
    processCount = numberOfProcess(w)
    #print(processCount)

    button = QPushButton('type button', w)
    button.setToolTip('This is an example button')
    button.move(100,70)
    #button.clicked.connect(onClick(w))
    button.clicked.connect(w.onClick)
    button.show()

    
    sys.exit(app.exec_())

