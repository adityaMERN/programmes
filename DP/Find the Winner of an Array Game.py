arr=list(map(int,input().split(" ")))
n=int(input())
d={}
k=0
while k!=n:
    if arr[0]>arr[1]:
        arr.remove(arr[1])
        arr.append(arr[1])
        if arr[0] not in d:
            d[arr[0]]=1
        else:
            d[arr[0]]+=1
    else:
        arr.remove(arr[0])
        arr.append(arr[0])
        if arr[0] not in d:
            d[arr[0]]=1
        else:
            d[arr[0]]+=1
    for 
