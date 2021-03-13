x=str(input())
y=str(input())
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
                if x[i-1]==y[j-1]:#agar dono ka last charater same hua toh
                    t[i][j]=1+t[i-1][j-1]
                else:#agar nahi hua same to do condition ,usme se jo maxx hoga wo choose krenge
                    t[i][j]=max(t[i-1][j],t[i][j-1])
    i=m
    j=n
    s=""
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            s+=x[i-1]
            i-=1
            j-=1
        else:
            if t[i-1][j]>t[i][j-1]:
                
                i-=1
            else:
                
                j-=1
    
    return s[::-1]
x=lcs(x,y,m,n)
print(x)