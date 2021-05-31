t=int(input())
for _ in range(t):
    n,m=map(int,input().split(" "))
    counter=0
    l=[1]*(n+1)
    # print(l)
    for j in range(2,n+1):
        a=m%j
        counter+=l[a]
        for k in range(a,n+1,j):
            l[k]+=1
    print(counter)