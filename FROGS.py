#question link:https://www.codechef.com/FEB21C/problems/FROGS
import math
t=int(input())
for _ in range(t):
    n=int(input())
    weight=list(map(int,input().split(" ")))
    length=list(map(int,input().split(" ")))
    d={}
    summ=0
    for i in range(1,n+1):
        d[i]=weight.index(i)
    #print(d)
    for i in range(2,n+1):
        x=d[i]
        y=d[i-1]
        a=0
        if x<=y:
            a=(math.ceil((y+1-x)/length[x]))
        summ+=a
        d[i]+=a*(length[x])
    print(summ)

    