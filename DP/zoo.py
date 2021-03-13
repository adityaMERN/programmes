import sys
import math
import random

s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
s3 = list(map(int, input().split()))
s4 = list(map(int, input().split()))
s5 = list(map(int, input().split()))

t3 = int(input())
c1 = s1[0]
c2 = s1[1]
c3 = s1[2]
a1 = s2[0]
a2 = s2[1]
a3 = s2[2]

m1 = s3[0]
ma1 = s3[1]
m2 = s4[0]
ma2 = s4[1] 
m3 = s5[0]
ma3 = s5[1]

n = max(c1, c2, c3)
if n == c1:
 
 j = m1 * ma1
elif n == c2:
 
 j = m2 * ma2
else:
 
 j = m3 * ma3
q = j*n



n = min(c1, c2, c3)
if n == c1:
    p = a1 * n
    i = a1
elif n == c2:
    p = a2 * n
    i = a2
else:
    p = a3 * n
    i = a3




k = t3 - (i + j)
l = []
l.append(c1)
l.append(c2)
l.append(c3)

r = k * sorted(l)[1]
# print(a3, z)

print(p+q+r)