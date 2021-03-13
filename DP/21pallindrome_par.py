import math
s=str(input())
#n=len(s)
def palPart(s,i,j):
    n=len(s)
    t=[[-1 for a in range(n+1)] for b in range(n+1)]
    if i>=j:
        return 0
    if s==s[::-1]:
        return 0
    if t[i][j]!=-1:
        return t[i][j]
    if t[i][j]==-1:
        ans=math.inf
        for k in range(i,j):
            if t[i][k]!=-1:
                left=t[i][k]
            else:
                left=palPart(s,i,k)
                t[i][k]=left
            if t[k+1][j]!=-1:
                right=t[k+1][j]
            else:
                right=palPart(s,k+1,j)
                t[k+1][j]=right
            temp=1+left+right
            ans=min(ans,temp)
        t[i][j]=ans
    #print(t)
    return ans
x=palPart(s,0,len(s)-1)
print(x)