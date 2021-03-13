n=int(input())
weight=list(map(int,input().split(" ")))
value=list(map(int,input().split(" ")))
w=int(input())

#recursive plus memoization
#t = [[-1 for i in range(w + 1)] for j in range(n + 1)] 
#print(t)
def knapsack(weight,value,w,n):
    t=[[0 for i in range(w+1)] for j in range(n+1)]
    #if n==0 or w==0:
        #return 0
    #if t[n][w]!=-1:
        #return t[n][w]
    #if weight[n-1]<=w:
        #t[n][w]=max((value[n-1]+knapsack(weight,value,w-weight[n-1],n-1)),knapsack(weight,value,w,n-1))
        #return t[n][w]
    #elif weight[n-1]>w:
        #t[n][w]=knapsack(weight,value,w,n-1)
        #return t[n][w]

#top-down approach
#print(t)
    for i in range(n+1):
        for j in range(w+1):
            if i==0 or j==0:
                t[i][j]=0
            elif weight[n-1]<=w:
                t[i][j]=max(value[i-1]+t[i-1][j-weight[i-1]],t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    return t[n][w]
print(knapsack(weight,value,w,n))
