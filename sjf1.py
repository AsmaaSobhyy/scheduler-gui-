
class Process:
     def __init__(self,pid,at,bt):
        self.pid=pid
        self.arrival=at
        self.burst=bt

chart = []

def SJF(plist,n,preemp):

   global chart
   queue=[]
   time=0
   ap=0 #arrival process
   rp=0 #ready process
   done=0 #done process
   
   if not preemp:
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

        if queue[0].burst>0:
              for g in range(queue[0].burst):
                  chart.append(queue[0].pid)
              time+=queue[0].burst
              queue[0].burst=99999999999 #burst finished bt=0
              done+=1
              rp+=1
              

   else:#preemp
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

        if queue[0].burst>0:
            
                    chart.append(queue[0].pid)
                    time+=1
                    queue[0].burst-=1
                    if queue[0].burst<1:
                     queue[0].burst=99999999999
                     done+=1
                     rp-=1



#test and print chart for non preemp put 0 and for preem put 1
plist=[]
plist.append(Process(1,1,7))
plist.append(Process(2,2,5))
plist.append(Process(3,3,1))
plist.append(Process(4,4,2))
plist.append(Process(5,5,8))

SJF(plist,len(plist),1)
print(chart)