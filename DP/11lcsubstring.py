x=str(input())
y=str(input())
m=len(x)
n=len(y)
def lcs(x,y,m,n):
    t=[[0 for j in range(n+1)]for i in range(m+1)]#base condition 
    #choice diagram
    res=0
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:#modification jo chahiye
                t[i][j]=0
            else:
                if x[i-1]==y[j-1]:#agar dono ka last charater same hua toh
                    t[i][j]=1+t[i-1][j-1]
                    res=max(res,t[i][j])
                else:#agar nahi hua same to do condition ,usme se jo maxx hoga wo choose krenge
                    t[i][j]=0
    print(t)
    return res
x=lcs(x,y,m,n)
print(x)