import math
arr=list(map(int,input().split(" ")))
#i=1
#j=len(arr)-1
t=[[-1 for y in range(101)]for x in range(101)]
def mcm(arr,i,j):
    n=len(arr)
    #temp=0
    
    #print(t,"\n")
    #base condition
    if i==j:
        t[i][j]=0
        return 0
    if t[i][j]!=-1:
        return t[i][j]
    ans=math.inf
    for k in range(i,j):
        temp=mcm(arr,i,k)+mcm(arr,k+1,j)+(arr[i-1]*arr[k]*arr[j])
            #print(temp)
        ans=min(ans,temp)
    
    t[i][j]=ans
    
    return ans
answer=mcm(arr,1,len(arr)-1)
print(answer)
for i in range(1,len(arr)):
    #for j in range(1,len(arr)):
        print(t[i][:len(arr)])
    