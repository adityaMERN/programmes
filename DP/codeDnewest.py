import math
import sys
from itertools import combinations
import random
nw = {
               100: "hundred",
               90:  "ninety", 80:  "eighty", 70:  "seventy",
               60:  "sixty", 50:  "fifty", 40:  "forty",
               30:  "thirty", 20:  "twenty", 19: "nineteen",
               18:  "eighteen", 17: "seventeen", 16: "sixteen",
               15:  "fifteen", 14: "fourteen", 13: "thirteen",
               12:  "twelve", 11:  "eleven", 10:  "ten",
               9:   "nine", 8:   "eight", 7:   "seven",
               6:   "six", 5:   "five", 4: "four", 3: "three",
               2: "two", 1: "one",0:"zero"
        }
def numberToWords(n):
        if n <= 20: 
            return nw[n]
        if n==100:
            return "hundred"
        for div in nw:
            d, r = divmod(n, div)
            if not d: continue
            s1 = numberToWords(d) if div >= 100 else ""
            s2 = numberToWords(r) if r else ""
            return s1 +nw[div] +s2
#print(numberToWords())
Table=[]
for i in range(101):
    Table.append(numberToWords(i))
#print(Table)
d={}
for i in range(101):
    d[i]= numberToWords(i)
#print(d[99])
vowel=['a','e','i','o','u']
n=int(input())
number=list(map(int,input().split(" ")))
c=0
for num in number:
    for char in d[num]:
        if char in vowel:
            c+=1
#print(c)
m=0
for i in range(n-1):
    for j in range(i+1,n):
        if number[i]+number[j]==c:
            m+=1
            #print((number[i],number[j]))
#print(m)
if m<=100:
    print(d[m],end="")
else:
    print("greater than 100",end="")