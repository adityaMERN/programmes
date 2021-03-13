a=str(input())
b=str(input())
m=len(a)
n=len(b)
def pscs(a,b,m,n):
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
    #upto here we simply create a matrix
    i=m
    j=n
    s=""
    while i>0 and j>0:
        if a[i-1]==b[j-1]:#if the charactera are same then we add it to s
            s+=a[i-1]
            i-=1
            j-=1
        else:
            if t[i][j-1]>t[i-1][j]:#if characters are not same and the value of its adacent box,whichever is max the charcter corresponding to it will be added to s
                s+=b[j-1]
                j-=1
            else:
                s+=a[i-1]
                i-=1
    while i>0:#to check if we ran out of one or any other string
        s+=a[i-1]
        i-=1
    while j>0:
        s+=b[j-1]
        j-=1
    return s[::-1]
x=pscs(a,b,m,n)
print(x)
