#january circuit 2021
#hackerearth


t=int(input())
for _ in range(t):
    x1,y1=map(int,input().split(" "))
    x2,y2=map(int,input().split(" "))
    if (x1-x2==0 and y1-y2==0):
        print("SECOND")
        continue
    elif abs(x1-x2)<=1 and abs(y1-y2)<=1:
        print("FIRST")
        continue
    else:
        print("DRAW")