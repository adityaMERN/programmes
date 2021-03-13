#author PRIYAMVADA SINGH CHAUHAN
import math  
import random
import itertools
import sys
t=int(input())
while t>0:
    #def Calculation(num,n)
    #taking the input
    n=int(input())
    l=list(map(int,input().split(" ")))
    no_use_array=[]
    no_use_array2=[]
    #defining variables
    numberOfZeroes=0
    numberOfTwos=0
    numberOfOnes=0
    anotherVariable=0
    if n%2==1:
        anotherVariable=1
        #starting the for loop
    secondVariable=0
    for i in range(n):
        secondVariable=l[i]%3
        if secondVariable==0:
            numberOfZeroes+=1
    newVariable=n//2
    if anotherVariable==0:
        if newVariable==numberOfZeroes:
            print("Yes")
        else:
            print("No")
    elif anotherVariable==1:
        if newVariable+1==numberOfZeroes:
            print("Yes")
        else:
            print("No")
    t-=1