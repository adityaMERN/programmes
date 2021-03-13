n=int(input())
l=list(map(int,input().split()))
s=int(input())
index=[]
for i in range(s):
    ind=int(input())
    index.append(ind)
for i in index:
    x=l.pop(i-1)
    print(x)
