# https://www.codechef.com/LTIME94B/problems/RACINGEN
t=int(input())
for _ in range(t):
    x,r,m=map(int,input().split(" "))
    r=r*60
    m=m*60
    if r<=x:
        final=r
    else:
        final=x+2*(r-x)
    if final<=m:
        print("YES")
    else:
        print("NO") 