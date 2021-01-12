#january 2021 long challenge first question

t=int(input())
for _ in range(t):
    n,k,d=map(int,input().split(" "))
    l=list(map(int,input().split(" ")))
    summation=sum(l)
    if summation//k >=d:
        print(d)
    else:
        print(summation//k)
        