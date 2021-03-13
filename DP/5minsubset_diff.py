arr=list(map(int,input().split(" ")))
def minsubsetdiff(arr):
    n=len(arr)
    ranger=sum(arr)
    t=[[False for j in range(ranger+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(ranger+1):
            if j==0:
                t[i][j]=True
            elif i==0:
                t[i][j]=False
            else:
                if arr[i-1]<=j:
                    t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]
    #print(t)
    final=[]
    for j in range((ranger//2)+1):
        if t[n][j]==True:
            final.append(j)
    #print(final)
    mn=99999999
    for k in final:
        mn=min(mn,(ranger-(2*k)))
        #print(mn)
    return mn
x=minsubsetdiff(arr)
print(x)
     
    