from os1 import *
def FCFS(self,num):
    process=[]
    for j in range (0,num):
        arr, okPressed = QInputDialog.getInt(self, "Get integer",f"process {j} arrive time:",0, 0, 100, 1)
        burst, okPressed = QInputDialog.getInt(self, "Get integer",f"process {j} burst timt:",0, 0, 100, 1)
        process.append({'arr':arr,'burst':burst,"number":j})
    
    final = sorted(process, key=lambda k: k['arr'])
    #print(final)
    wt=0
    current=0
    for km in range (1,num):
        wt+=(current + final[km-1]['burst'] )-(final[km]['arr'])
        current += final[km-1]['burst'] 
    #print(wt)
    start=0
    average=wt/num
    draw1 = QDialog()
    draw1.setWindowTitle("FCFS")
    draw1.setModal(True)
    for g in range(0,num):
        #print(chart[g])
        #print(protime[g]) 
        k=  final[g]['number']
        button1 = QPushButton(f'process{k}', draw1 )
        button1.move(start,10)
        #x=5*sortedProcess[g]['burst']
        button1.resize(100,20)
        k=final[g]['burst']
        l=QLabel(f'{k}',draw1)
        l.move(start+45,30)
        l.show()
        start= start+100
        button1.show()  

    l1=QLabel(f'average waiting time =  {average}',draw1)
    l1.move(50,100)
    l1.show()
    #l.setText("Hello World") 
    draw1.exec()