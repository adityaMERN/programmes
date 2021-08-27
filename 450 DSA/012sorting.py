#https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1

arr=list(map(int,input().split(" ")))
d={}
d={}
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
i=0
for k in d:
    if k==0:
        a0=d[k]
    elif k==1:
        a1=d[k]
    elif k==2:
        a2=d[k]
while a0>0:
    arr[i]=0
    i+=1
    a0-=1
while a1>0:
    arr[i]=1
    i+=1
    a1-=1
while a2>0:
    arr[i]=2
    i+=1
    a2-=1
print(arr)