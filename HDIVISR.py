#Link: https://www.codechef.com/FEB21C/problems/HDIVISR

import math
n=int(input())
i = 1
l=[]
while i <= math.sqrt(n):
    if (n % i == 0) :
        if (n / i == i) :
            l.append(i) 
        else :
            l.append(i)
            l.append(n//i)  
    i = i + 1
newlist=[]
for i in range(len(l)):
    if l[i]<=10:
        newlist.append(l[i])
print(max(newlist))