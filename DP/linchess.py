import math
t=int(input())
for _ in range(t):
    n,k=map(int,input().split(" "))
    l=list(map(int,input().split(" ")))
    checkList=[]
    l.sort()
    
    #variable=math.inf
    for i in l:
        if i<=k and k%i==0:
            checkList.append([k//i-1,i])
    #print(checkList)
    if len(checkList)>=1:
        checkList.sort(key = lambda x: x[0])
        print(checkList[0][1])
    else:
        print("-1")

