x=str(input())
y=x
m=len(x)
n=len(y)
def lcs(x,y,m,n):
    t=[[0 for j in range(n+1)]for i in range(m+1)]#base condition 
    #choice diagram
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:#modification jo chahiye
                t[i][j]=0
            else:
                if x[i-1]==y[j-1] and i!=j:
                    t[i][j]=1+t[i-1][j-1]
                else:#agar nahi hua same to do condition ,usme se jo maxx hoga wo choose krenge
                    t[i][j]=max(t[i-1][j],t[i][j-1])
    return t[m][n]
x=lcs(x,y,m,n)
print(x)