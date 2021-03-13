t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split(" ")))
    newlist=[]
    for i in range(n-1):
        for j in range(i+1,n):
            if abs(arr[i]-arr[j])<=1:
                if arr[i]<arr[j]:
                    arr.remove(arr[i])
                elif arr[j]<arr[i]:
                    arr.remove(arr[j])
                else:
                    arr.remove(arr[i])
    print(arr)
                


