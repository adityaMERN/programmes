coin=list(map(int,input().split(" ")))
price=int(input())
def coinchange(coin,price):
    t=[[0 for j in range(price+1)] for i in range(len(coin)+1)]
    for i in range(len(coin)+1):
        for j in range(price+1):
            if j==0:
                t[i][j]=1
            elif i==0:
                t[i][j]=0
            else:
                if coin[i-1]<=price:
                    t[i][j]=t[i][j-coin[i-1]]+t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]
    print(t)
    return t[len(coin)][price]
x=coinchange(coin,price)
print(x)