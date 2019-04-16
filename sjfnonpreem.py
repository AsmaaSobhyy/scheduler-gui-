from os1 import *
class Process:
     def __init__(self,pid,at,bt):
        self.pid=pid
        self.arrival=at
        self.burst=bt

# chart = []

def SJF(self,n):
    plist=[]
    chart = []
    for j in range (0,n):
        arr, okPressed = QInputDialog.getInt(self, "Get integer",f"process {j} arrive time:",0, 0, 100, 1)
        burst, okPressed = QInputDialog.getInt(self, "Get integer",f"process {j} burst timt:",0, 0, 100, 1)
        plist.append(Process(j,arr,burst))

    #print(plist)
#    global chart
    queue=[]
    protime=[]
    waiting=0
    time=0
    ap=0 #arrival process
    rp=0 #ready process
    done=0 #done process
   
   
   #check for new process
    while(done<n):
        for i in range (ap,n):
            if time>=plist[i].arrival:
                queue.append(plist[i])
                ap+=1
                rp+=1
   #if no process put 0 in chart
        if rp<1:
            time+=1
            chart.append(0)
            continue
          
    #sort by burst time and if burst of two process equel sort by arrival

        queue.sort(key=lambda x: (x.burst,x.arrival))
        #print(queue)
        if queue[0].burst>0:
            chart.append(queue[0].pid)
            protime.append(queue[0].burst)
            # for g in range(queue[0].burst):
            #     chart.append(queue[0].pid)
            waiting+=(time-queue[0].arrival)
            time+=queue[0].burst
            queue[0].burst=99999999999999999 #burst finished bt=0
            done+=1
            rp+=1
                  
    start=0
    #print(chart)
    #print(protime)
    average = waiting/n
    #print(average)
    #print(n)
    draw1 = QDialog()
    draw1.setWindowTitle("SJF non-Preemptive")
    draw1.setModal(True)
    for g in range(0,n):
        #print(chart[g])
        #print(protime[g]) 
        k=  chart[g]
        button1 = QPushButton(f'process{k}', draw1 )
        button1.move(start,10)
        #x=5*sortedProcess[g]['burst']
        button1.resize(100,20)
        k=protime[g]
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
    # print(waiting)
    # print(average)    
 

#test and print chart for non preemp put 0 and for preem put 1
# plist=[]


# plist.append(Process(1,1,7))
# plist.append(Process(2,2,5))
# plist.append(Process(3,3,1))
# plist.append(Process(4,4,2))
# plist.append(Process(5,5,8))

# SJF(plist,len(plist))
# print(chart)
 


