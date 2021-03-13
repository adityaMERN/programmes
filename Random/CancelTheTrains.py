t=int(input())
for _ in range(t):
    n,m=map(int,input().split(" "))
    bottom=list(map(int,input().split(" ")))
    left=list(map(int,input().split(" ")))
    bottom_set=set(bottom)
    left_set=set(left)
    x=len(bottom_set.intersection(left_set))
    print(x)