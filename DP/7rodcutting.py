length=list(map(int,input().split(" ")))
price=list(map(int,input().split(" ")))
#n=int(input())
def rod(length,price):
    #t[len(pricearray)+1][totallength jo chahiye]
    t=[[0 for j in range(len(length)+1)] for i in range(len(price)+1)]
    for i in range(len(price)+1):
        for j in range(len(length)+1):
            if j==0:
                t[i][j]=0
            elif i==0:
                t[i][j]=0
            else:
                if length[i-1]<=j:
                    t[i][j]=max(price[i-1]+t[i][j-length[i-1]],t[i-1][j])
                else:
                    t[i][j]=t[i-1][j]
    print(t)
    return t[len(price)][len(length)]
x=rod(length,price)
print(x)