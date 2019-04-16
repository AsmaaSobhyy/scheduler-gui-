# implement fcfs cpu scheduling                                                       

n = []
bt = []  #burst time
at = []
temp=[]
wt = [0,0,0,0,0,0,0,0,0]
tat = [0,0,0,0,0,0,0,0,0,0]

#take input
for i in range(0,n):
    bt.append(bt[i])

#take arrival time
for i in range(0,n):
        at.append(at[i])
temp[0] = 0

for i in range(0,n):
    wt[i]=0
    tat[i]=0
    temp[i+1]= temp[i]+bt[i]
    wt[i]=temp[i]-at[i]


#waiting time
#for i in range (1,n) :
      # wt[i]=temp[i]-at[i]
#turn around time
for i in range(0,n):
    tat[i] = wt[i] + bt[i]

print()
print("\tProcess\t\tArrival Time\t\tBurst Time\t\tWaiting Time\t\tTurn Around Time")
for i in range(0,n):
    print(f"\t  {i}\t\t   {at[i]}\t\t   {bt[i]}\t\t\t  {wt[i]}\t\t               {tat[i]}")
