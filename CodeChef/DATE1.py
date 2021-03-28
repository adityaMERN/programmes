#https://www.codechef.com/LTIME94B/problems/DATE1

t=int(input())
for _ in range(t):
    a,y,x=map(int,input().split(" "))
    if a>=y:
        print(y*x)
    else:
        print(a*x+1)