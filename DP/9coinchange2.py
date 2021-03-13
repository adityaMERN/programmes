import sys
coin=list(map(int,input().split(" ")))
summ=int(input())
def dp(coin,summ):
    t=[[0 for j in range(summ+1)] for i in range(len(coin)+1)]
    for i in range(len(coin)+1):
        for j in range(summ+1):
            if i==0:
                t[i][j]=sys.maxsize
            elif j==0:
                t[i][j]=0
            elif i==1 and j!=0:
                #pehla elememnt coin array se uthaaenge orr check krenge ki j jo sum hai usse mod ho rha hai ya nhi...
                if j%coin[0]==0:
                    t[i][j]=j//coin[0]
                else:
                    t[i][j]=sys.maxsize
            else:
                if coin[i-1]<=j:
                    t[i][j]=min(t[i-1][j],1+t[i][j-coin[i-1]])
                else:
                    t[i][j]=t[i-1][j]
    return t[len(coin)][summ]
x=dp(coin,summ)
print(x)