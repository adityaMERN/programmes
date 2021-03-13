import math
n=int(input())
l=[]
c=0
for i in range(n):
    x=list(map(str,input().split(" ")))
    l.append(x)
for j in range(n):
    for k in range(n):
        if l[j][k]=="D":
            c+=1
print(math.floor(math.sqrt(c)))
