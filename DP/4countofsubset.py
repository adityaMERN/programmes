arr=list(map(int,input().split(" ")))
summ=int(input())
def subsetcount(arr,summ):
    t=[[0 for j in range(summ+1)]for i in range(len(arr)+1)]
    #print(t)
    for i in range(len(arr)+1):
        for j in range(summ+1):
            if j==0:
                t[i][j]=1
            elif i==0:
                t[i][j]=0
            else:
                if arr[i-1]<=j:
                    t[i][j]=t[i-1][j-arr[i-1]]+t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]
    print(t)
    return t[len(arr)][summ]
x=subsetcount(arr,summ)
print(x)