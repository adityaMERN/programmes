from collections import Counter
a=str(input())
b=str(input())
m=len(a)
n=len(b)
def lcs(a,b,m,n):
    t=[[0 for j in range(n+1)]for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j]=0
            else:
                if a[i-1]==b[j-1]:
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])
    #i=m
    #j=n
    #s=""
    #while i>0 and j>0:
        #if a[i-1]==b[j-1]:
            #s+=a[i-1]
            #i-=1
            #j-=1
        #else:
            #if t[i-1][j]>t[i][j-1]:
                #i-=1
            #else:
                #j-=1
    #return s[::-1]
    return m+n-t[m][n]
x=lcs(a,b,m,n)
#y=a+b-x
#submerge=list(a+b)
#common=list(x)
#res = list((Counter(submerge)-Counter(common)).elements())
#print(res)
print(x)