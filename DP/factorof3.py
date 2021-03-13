#author PRIYAMVADA SINGH CHAUHAN
import math  
import sys
import random
t=int(input())
for _ in range(t):
    #def Calculation(num,n)
    #taking the input
    def Calculator(num,n):
        #defining variables
        numberOfZeroes=0
        #numberOfTwos=0
        #numberOfOnes=0
        anotherVariable=0
        if n%2==1:
            anotherVariable=1
        #starting the for loop
        secondVariable=0
        for i in range(n):
            secondVariable=num[i]%3
            if secondVariable==0:
                numberOfZeroes+=1
        newVariable=n//2
        if anotherVariable==0:
            if newVariable==numberOfZeroes:
                return "Yes"
            else:
                return "No"
        elif anotherVariable==1:
            if newVariable+1==numberOfZeroes:
                return "Yes"
            else:
                return "No"

    #condition checking:
    
    n=int(input())
    num=list(map(int,input().split(" ")))
    #no_use_array=[]
    #no_use_array2=[]
    x=Calculator(num,n)
    print(x,end="\n")
    
    
#




