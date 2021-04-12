#https://www.codechef.com/RTR2021/problems/CMACHINE

t=int(input())
for _ in range(t):
    x=int(input())
    prod=1
    for i in range(1,x+1):
        prod*=i
    print(prod)
