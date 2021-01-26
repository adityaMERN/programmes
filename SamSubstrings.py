# Question link:  https://www.hackerrank.com/challenges/sam-and-substrings/problem

#solution:
import math
import os
import random
import re
import sys

# Complete the substrings function below.
def substrings(n):
    modd=(10**9+7)
    x=len(n)
    a=[]
    a.append(1)
    #print(a[0])
    #a[0]=1
    #b[0]=1
    b=[]
    b.append(1)
    #print(b[0])
    for i in range(1,x):
        a.append((10*a[i-1])%modd)
        b.append((b[i-1]+a[i])%modd)
    ans=0
    for i in range(x):
        ans+=((int(n[i])-int("0"))*b[x-i-1]*(i+1))%modd
        ans%=modd
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
