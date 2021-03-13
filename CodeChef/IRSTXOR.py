#question link: https://www.codechef.com/MARCH21B/problems/IRSTXOR

import math
t=int(input())
for _ in range(t):
    n=int(input())
    summ=0
    a=1
    while n>=summ:
        summ=math.pow(2,a)
        a+=1
    a-=1
    a-=1
    k=math.pow(2,a)
    k-=1
    u=summ-n
    answer=k*(k+u)
    print(int(answer))