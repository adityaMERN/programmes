#author ADITYA ANAND
import math  
import random

import sys
#to find the largest possible factor for the given number  
def findFactor(value): 
    factor=[]
    answer=[]
    for i in (range(2, int(math.sqrt(value))+1)):
          if value%i==0:
            return (value//i)
    return 1
#this is our main function           
number1,number2=map(int,input().split())
inputList=[]
inputList.append(number1)
inputList.append(number2)
#making a list to find the factor of first number
factorOfNumber1=[]
x1=inputList[0]
#if the number is equal to 1 then just append 1
if x1==1:
    factorOfNumber1.append(1)
#if the number is greater than 1 then we will find its greatest factor again and again and append it to the facto1 list
else:
    while(x1>1):
        factorOfNumber1.append(findFactor(x1))
        x1=findFactor(x1)
#making a list named as factor of number 2
factorOfNumber2=[]
x2=inputList[1]
if x2==1:
    factorOfNumber2.append(1)
else:
    while(x2>1):
        factorOfNumber2.append(findFactor(x2))
        x2=findFactor(x2)

#if same then print 0
if(inputList[0]==inputList[1]):
    output=0

elif inputList[0] in factorOfNumber2:
    output=factorOfNumber2.index(inputList[0])+1
elif inputList[1] in factorOfNumber1:
    output=factorOfNumber1.index(inputList[1])+1
else:
    common=list(set(factorOfNumber1) & set(factorOfNumber2))
    common.sort(reverse=True)
    gcd=common[0]
    output=factorOfNumber1.index(gcd)+factorOfNumber2.index(gcd)+2
#output window
print(output)