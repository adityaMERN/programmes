t=int(input())
for _ in range(t):
    h,p=map(int,input().split(" "))
    h=h-p
    while p>1:
        p=p//2
        h=h-p
        if h<0:
            break
    if h>0:
        print("0")
    else:
        print("1")
