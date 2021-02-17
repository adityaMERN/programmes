#question link: https://www.codechef.com/FEB21C/problems/PRIGAME
#segmented-seive
import math
# prime = []
# def simpleSieve(limit):
#     mark = [True for i in range(limit + 1)]
#     p = 2
#     while (p * p <= limit):
#         if (mark[p] == True): 
#             for i in range(p * p, limit + 1, p): 
#                 mark[i] = False 
#         p += 1
#     l=[]
#     for p in range(2, limit): 
#         if mark[p]:
#             prime.append(p)
#             l.append(p)
#             #print(p,end = " ")
#     return l
# def segmentedSieve(n):
#     limit = int(math.floor(math.sqrt(n)) + 1)
#     xx=simpleSieve(limit)
#     low = limit
#     high = limit * 2
#     while low < n:
#         if high >= n:
#             high = n
#         mark = [True for i in range(limit + 1)]
#         for i in range(len(prime)):
#             loLim = int(math.floor(low / prime[i]) *
#                                          prime[i])
#             if loLim < low:
#                 loLim += prime[i]
#             for j in range(loLim, high, prime[i]):
#                 mark[j - low] = False
#         yy=[]
#         for i in range(low, high):
#             if mark[i - low]:
#                 yy.append(i)
#                 #print(i, end = " ")
#         low = low + limit
#         high = high + limit
#     return xx+yy

# t=int(input())
# for _ in range(t):
#     x,y=map(int,input().split(" "))
#     length=len(segmentedSieve(x))
#     if length<=y:
#         print("Chef")
#     else:
#         print("Divyam")

def is_Prime(n):
    for i in range(2,int(math.floor(math.sqrt(n)) + 1)):
        if n%i==0:
            return False
    return True
t=int(input())
count=0
dp=[0 for i in range(1000001)]
for i in range(2,1000001):
    if is_Prime(i):
        count+=1
    dp[i]=count
for _ in range(t):
    x,y=map(int,input().split(" "))
    if dp[x]<=y:
        print("Chef")
    else:
        print("Divyam")

