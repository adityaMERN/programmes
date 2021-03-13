#https://www.codechef.com/COOK126C/problems/MANYSUMS

t=int(input())
for _ in range(t):
    l,r=map(int,input().split(" "))
    maximum=2*r
    minimum=2*l
    print(maximum-minimum+1)
