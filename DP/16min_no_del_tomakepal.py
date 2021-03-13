a=str(input())
b=a[::-1]
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
                    t[i][j]=max(t[i][j-1],t[i-1][j])
    print(t)
    return t[m][n]
x=lcs(a,b,m,n)
print(m-x)