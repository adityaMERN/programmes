t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split(" ")))
    count=0
    for i in range(n-1):
        for j in range(i,n):
            #print((i,j))
            x=l[i]&l[j]
            if x==l[i] and i<j:
                count+=1
    print(count)