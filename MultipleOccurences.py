#december circuit first question
#not done
import math
def findIndex (a,n,key): 
    start = -1
    for i in range(n): 
        if a[i] == key: 
            start = i 
            break
    if start == -1: 
        #print("Key not present in array") 
        return 0 
    end = start 
    for i in range(n-1, start - 1, -1): 
        if a[i] == key: 
            end = i 
            break
    if start == end: 
        return [start+1,0+1] 
    else: 
        return [start+1,end+1] 


t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split(" ")))
    d=set(l)
    keys=[]
    for key in d:
        keys.append(key)
    #print(keys)
    summation=[]
    for element in keys:
        answer=findIndex(l,n,element)
        #print(answer)
        diff=abs(answer[0]-answer[1])
        summation.append(diff)
    #print(summation)
    print(sum(summation))

