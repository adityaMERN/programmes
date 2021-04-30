import math
n=int(input())
i=1
l=[]
while i<=math.sqrt(n):
    if n%i==0:

        l.append(n//i)
        if i not in l:
            l.append(i)
    i+=1
#
l.sort()
#print(l)
print(len(l))
print(*l)       