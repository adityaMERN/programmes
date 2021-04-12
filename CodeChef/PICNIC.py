t=int(input())
for _ in range(t):
    n=int(input())
    p=list(map(int,input().split(" ")))
    count=0
    for i in range(1,len(p)):
        if p[i]<=p[i-1]:
            count+=(p[i-1]-p[i])
    print(count)
