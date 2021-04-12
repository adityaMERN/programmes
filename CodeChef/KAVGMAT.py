#https://www.codechef.com/APRIL21B/KAVGMAT
def function(matrix,n,m,k,order):
    c=0
    minimum=min(n,m)
    while order< minimum+1:
        i=order
        j=m
        while i<n+1:
            x=i-order+1
            y=j-order+1
            z=matrix[i][j]-matrix[x-1][j]-matrix[i][y-1]+matrix[x-1][y-1]
            if z//(order*order)<k:
                i+=1
            else:
                start=0
                end=m
                while start<=end:
                    mid=(start+end)//2
                    x=i-order+1
                    y=mid-order+1
                    z=matrix[i][mid]-matrix[x-1][mid]-matrix[i][y-1]+matrix[x-1][y-1]
                    if z//(order*order)<k:
                        start=mid+1
                    else:
                        ans=mid
                        end=mid-1
                c+=m-ans+1
                i+=1
        order+=1
    return c



t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split(" "))
    matrix=[]
    matrix.append([0]*(m+1))
    for i in range(n):
        row=list(map(int,input().split(" ")))
        row.insert(0,0)
        matrix.append(row)
    #print(matrix)
    for i in range(1,n+1):
        summ=0
        for j in range(1,m+1):
            summ+=matrix[i][j]
            matrix[i][j]=summ
    for i in range(1,m+1):
        summ=0
        for j in range(1,n+1):
            summ+=matrix[j][i]
            matrix[j][i]=summ
    answer=function(matrix,n,m,k,1)
    print(answer)

