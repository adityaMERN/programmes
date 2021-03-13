import math
e=int(input())
f=int(input())
def solve(e,f):
    t=[[0 for jj in range(f+1)]for ii in range(e+1)]
    for z in range(1,e+1):
        t[z][1]=1
        t[z][0]=0
    for aa in range(1,f+1):
        t[1][aa]=aa
    for i in range(2,e+1):
        for j in range(2,f+1):
            t[i][j]=math.inf
            for k in range(1,f+1):
                temp=1+max(t[i-1][k-1],t[i][j-k])
                if temp<t[i][j]:
                    t[i][j]=temp
    return t[e][f]
x=solve(e,f)
print(x)