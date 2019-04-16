chart = []
class Process:
    def __init__(self, pid, At, Bt):
        self.pid = pid
        self.arrival = At
        self.burst = Bt
#-----------------------------circular shift left--------------------------------#
def shiftCL(alist):
    temp = alist[0]
    for i in range(len(alist)-1):
        alist[i]=alist[i+1]
    alist[len(alist)-1]=temp
    return alist
#---------------------------------round robin-------------------------------------#
def RR(tq,plist,n) :
    global chart
    queue=[]
    time=0
    ap=0    #arrived processes
    rp=0    #ready processes
    done=0  #done processes
    q=tq #time quantum
    start = 0
#------------------------------checking on process which done------------------------#    
    while(done<n):
        for i in range(ap,n):
            if time>=plist[i].arrival:
                queue.append(plist[i])
                ap+=1
                rp+=1
        if rp<1:
            chart.append(0)
            time+=1
            continue
        #shift
        if start:
            queue = shiftCL(queue)

        if queue[0].burst>0:
            if queue[0].burst>q:
                for g in range(time, time+q):
                    chart.append(queue[0].pid)
                time+=q
                queue[0].burst-=q
            else:
                for g in range (time, time+queue[0].burst):
                    chart.append(queue[0].pid)
                time+=queue[0].burst
                queue[0].burst=0
                done+=1
                rp-=1
            start=1         #flag
plist = []
#time Quantum,process list,no of process
plist.append(Process(1,0,5))
plist.append(Process(2,1,3))
plist.append(Process(3,3,6))
plist.append(Process(4,5,1))
plist.append(Process(5,6,4))

RR(3,plist,len(plist))
print(chart)

