# program to implement sjf(shortest job first ) cpu scheduling
n = int(input("Enter number of processes : "))
#initialize with zero to avoid errors
bt = [0] #burst time
p = [0,0,0,0,0,0,0,0,0,0,0,0,0]  # processes
wt = [0,0,0,0,0,0,0,0,0,0,0,0,0]  # waiting time
tat = [0,0,0,0,0,0,0,0,0,0,0,0,0]  # turn around time
for i in range(0,n):
     bt.append(int(input(f"Enter burst time for process {i} --> ")))
for i in range(0,n):
       for j in range(i+1,n):
              if bt[i]>bt[j]:
                     temp = bt[i]
                     bt[i] = bt[j]
                     bt[j] = temp

                     temp = p[i]
                     p[i] = p[j]
                     p[j] = temp

wt[0] = 0
tat[0] = bt[0]
for i in range (1,n):
   wt[i] = wt[i-1] + bt[i-1]
   tat[i] = tat[i-1] + bt[i]

print(" PROCESS\tBURST TIME\tTURN AROUND TIME")
print()
for i in range(0,n):
    print(f"      {i}\t\t  {bt[i]}\t\t       {wt[i]}\t\t         {tat[i]}")
    print()

# now its done
# let's check