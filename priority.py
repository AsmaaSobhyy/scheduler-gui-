from os1 import *
def priority(self,preemptive,num):
    process = []
    final=[]
    time=[]
    #print(preemptive)
    for j in range (0,num):
        arr, okPressed = QInputDialog.getInt(self, "Get integer",f"process {j} arrive time:",0, 0, 100, 1)
        burst, okPressed = QInputDialog.getInt(self, "Get integer",f"process {j} burst timt:",0, 0, 100, 1)
        prior, okPressed = QInputDialog.getInt(self, "Get integer",f"process {j} priority:",0, 0, 100, 1)
        process.append({'arr':arr,'burst':burst,'prior':prior,"number":j})
        if(preemptive):
            process[j]["rest"]=burst
    
    
    if preemptive:
        priorsort = sorted(process, key=lambda k: k['prior'])
        sortedProcess = sorted(process, key=lambda k: k['arr'])
    else:
        sortedProcess = sorted(process, key=lambda k: k['prior'])
    
    #print(sortedProcess)
    start=0
    current = 0
    finish=[]
    currentprior=200
    total =0
    here=0
    l=1
    time1=0
    totaltime=0
    f=0
    imp = sortedProcess[0]
    if not preemptive:
        for m in range (0,num):
            for n in range(0,num):
                if sortedProcess[n]['arr']<=current:
                    if sortedProcess[n] in final:
                        f=0
                    else:
                        final.append(sortedProcess[n])
                        time.append(sortedProcess[n]['burst'])
                        current +=sortedProcess[n]['burst']
            #print(final)

    else:
        for m in range (0,num):
            total += sortedProcess[m]['burst']
            finish.append({'finish':0})
        #print(total)
        for n in range (0,total+1):
            for m in range (0,num):
                if sortedProcess[m]['arr'] <= current :
                    if sortedProcess[m]['prior'] < currentprior and sortedProcess[m]['rest'] != 0:
                        currentprior=sortedProcess[m]['prior']
                        final.append(sortedProcess[m])
                        if(time1==0):
                            f=0
                        else:
                            time.append(time1)
                            totaltime += time1
                            time1=0
                        sortedProcess[m]['rest'] -=1
                        current +=1
                        time1 +=1

                        here=m
                        if sortedProcess[m]['rest'] == 0 and l != num:
                            currentprior=priorsort[l]['prior']+1
                            #finish.append({'number':m,'finish':current})
                            finish[m]['finish']=current
                            l+=1
                            

                        
                    elif sortedProcess[m]['prior'] == currentprior and sortedProcess[here]['rest'] != 0:
                        current +=1
                        time1 +=1
                        sortedProcess[here]['rest'] -=1
                        #print(sortedProcess[here]['rest'])
                        if sortedProcess[here]['rest'] == 0 and l != num:
                            currentprior=priorsort[l]['prior']+1
                            finish[here]['finish']=current
                            l+=1
                            
                       
                    

    
    #print(final)
    time.append(total-totaltime)
    print(time)
    current=0
    wt=0
    if(preemptive):
        for km in range (0,num):
            if finish[km]['finish']==0:
                finish[km]['finish']=total
            wt+=(finish[km]['finish'])-(sortedProcess[km]['arr'])-(sortedProcess[km]['burst'])
    else:
        for km in range (1,num):
            wt+=(current + final[km-1]['burst'] )-(final[km]['arr'])
            current += final[km-1]['burst'] 
    average = wt/num  
    #print(average)
    #print(final)
    size=len(final)
    #print(size)
    draw = QDialog()
    draw.setModal(True)
    
    for g in range(0,size): 
        k=final[g]['number']     
        button = QPushButton(f'process{k}', draw )
        button.move(start,10)
        #x=5*sortedProcess[g]['burst']
        button.resize(100,20)
        l=QLabel(f'{time[g]}',draw)
        l.move(start+45,30)
        l.show()
        start= start+100
        button.show()  

    l1=QLabel(f'average waiting time =  {average}',draw)
    l1.move(50,100)
    l1.show()
    #l.setText("Hello World") 
    draw.exec()    