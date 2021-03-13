#link: https://codeforces.com/contest/1493/problem/A

t=int(input())
for _ in range(t):
    n,k=map(int,input().split( " "))
    print(n-k+k//2,end="\n")
    l=[]
    m=[]
    for i in range(k+1,n+1):
        l.append(i)
    for i in range((k+1)//2,k):
        l.append(i)
   
    for i in range(len(l)):
        print(l[i],end=" ")

    