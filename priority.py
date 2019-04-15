from os1 import *
def priority(self,preemptive,num):
    process = []
    final=[]
    #print(preemptive)
    for j in range (0,num):
        arr, okPressed = QInputDialog.getInt(self, "Get integer",f"process {j} arrive time:",0, 0, 100, 1)
        burst, okPressed = QInputDialog.getInt(self, "Get integer",f"process {j} burst timt:",0, 0, 100, 1)
        prior, okPressed = QInputDialog.getInt(self, "Get integer",f"process {j} priority:",0, 0, 100, 1)
        process.append({'arr':arr,'burst':burst,'prior':prior,"number":j})
    sortedProcess = sorted(process, key=lambda k: k['prior'])
    #print(num)
    start=0
    current = 0
    f=0
    imp = sortedProcess[0]
    for m in range (0,num):
        for n in range(0,num):
            if sortedProcess[n]['arr']<=current:
                if sortedProcess[n] in final:
                    f=0
                else:
                    final.append(sortedProcess[n])
                    current +=sortedProcess[n]['burst']
        
    print(final)
    current=0
    wt=0
    for km in range (1,num):
        wt+=(current + final[km-1]['burst'] )-(final[km]['arr'])
        current += final[km-1]['burst'] 
    average = wt/num  
    print(average)
    for g in range(0,num): 
        k=final[g]['number']      
        button = QPushButton(f'process{k}', self )
        button.move(start,10)
        x=5*sortedProcess[g]['burst']
        button.resize(100,20)
        start= start+100
        button.show()       