fcfs function here
# implement fcfs cpu scheduling

n = int(input("Enter number of processes : "))
bt = []  #burst time
wt = [0,0,0,0,0,0,0,0,0]
tat = [0,0,0,0,0,0,0,0,0,0]
#take input
for i in range(0,n):
    bt.append(int(input(f"Enter burst time for process {i} ->")))
#waiting time
for i in range (1,n) :
    wt[i] = 0
    for j in range(0,i):
        wt[i] += bt[i]
#turn around time
for i in range(0,n):
    tat[i] = wt[i] + bt[i]

print()
print("\tProcess\t\tBurst Time\t\tWaiting Time\t\tTurn Around Time")
for i in range(0,n):
    print(f"\t  p[{i}]\t\t   {bt[i]}\t\t\t  {wt[i]}\t\t               {tat[i]}")
