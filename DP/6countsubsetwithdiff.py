arr=list(map(int,input().split(" ")))
diff=int(input())
s=sum(arr)
s1=(s+diff)//2
def susetcount(arr,s1):
    t=[[0 for j in range(s1+1)] for i in range(len(arr)+1)]
    for i in range(len(arr)+1):
        for j in range(s1+1):
            if j==0:
                t[i][j]=1
            elif i==0:
                t[i][j]=0
            else:
                if t[i][j]<=j:
                    t[i][j]=t[i-1][j-arr[i-1]] + t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]
    return t[len(arr)][s1]
x=susetcount(arr,s1)
print(x)
