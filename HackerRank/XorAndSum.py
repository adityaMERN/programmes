# https://www.hackerrank.com/challenges/xor-and-sum/problem

#!/bin/python3

import os
import sys

#
# Complete the xorAndSum function below.
#
def xorAndSum(a, b):
    #
    # Write your code here.
    #
    x=int(a,2)
    y=int(b,2)
    ans=0
    for i in range(314160):
        ans+=x^(y<<i)
    return ans%(10**9+7)

if __name__ == '__main__':
    

    a = input()

    b = input()

    result = xorAndSum(a, b)

    print(result)
