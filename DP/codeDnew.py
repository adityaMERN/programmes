import math
import sys
import random
#author: ADITYA ANAND
#creating manually a table for storing the values of the integers
l1=[[0,"zero"],[1,"one"],[2,"two"],[3,"three"],[4,"four"],[5,"five"],[6,"six"],[7,"seven"],[8,"eight"],[9,"nine"],[10,"ten"]]
l2=[[11,"eleven"],[12,"twelve"],[13,"thirteen"],[14,"fourteen"],[15,"fifteen"],[16,"sixteen"],[17,"seventeen"],[18,"eighteen"],[19,"nineteen"],[20,"twenty"]]
l3=[[21,"twenty-one"],[22,"twenty-two"],[23,"twenty-three"],[24,"twenty-four"],[25,"twenty-five"],[26,"twenty-six"],[27,"twenty-seven"],[28,"twentyeight"],[29,"twentynine"],[30,"thirty"]]
l4=[[31,'thirty-one'], [32,'thirty-two'], [33,'thirty-three'], [34,'thirty-four'], [35,'thirty-five'], [36,'thirty-six'], [37, 'thirty-seven'], [38, 'thirty-eight'], [39, 'thirty-nine'], [40, 'forty']]
l5=[[41, 'forty-one'], [42, 'forty-two'],[43, 'forty-three'], [44, 'forty-four'], [45, 'forty-five'], [46, 'forty-six'], [47, 'forty-seven'], [48, 'forty-eight'], [49, 'forty-nine'], [50, 'fifty']]
l6=[[51, 'fifty-one'], [52, 'fifty-two'], [53, 'fifty-three'], [54, 'fifty-four'], [55,'fifty-five'], [56, 'fifty-six'], [57,'fifty-seven'], [58, 'fifty-eight'], [59, 'fifty-nine'], [60, 'sixty']]
l7=[[61, 'sixty-one'], [62, 'sixty-two'], [63, 'sixty-three'], [64, 'sixty-four'], [65, 'sixty-five'], [66, 'sixty-six'], [67, 'sixty-seven'], [68, 'sixty-eight'], [69, 'sixty-nine'], [70, 'seventy']]
l8=[[71, 'seventy-one'], [72, 'seventy-two'], [73, 'seventy-three'], [74, 'seventy-four'], [75, 'seventy-five'], [76, 'seventy-six'], [77, 'seventy-seven'], [78, 'seventy-eight'], [79, 'seventy-nine'], [80, 'eighty']]
l9=[[81, 'eighty-one'],[82, 'eighty-two'], [83, 'eighty-three'], [84, 'eighty-four'], [85, 'eighty-five'], [86, 'eighty-six'], [87, 'eighty-seven'], [88, 'eighty-eight'], [89, 'eighty-nine'], [90, 'ninety']]
l10=[[91, 'ninety-one'], [92, 'ninety-two'], [93, 'ninety-three'], [94, 'ninety-four'], [95, 'ninety-five'], [96, 'ninety-six'], [97, 'ninety-seven'], [98, 'ninety-eight'], [99,'ninety-nine'], [100, 'hundred']]
newTable=l1+l2+l3+l4+l5+l6+l7+l8+l9+l10
#print(newTable)
#creating a dictionary
d={}
for i in newTable:
    d[i[0]]=i[1]
print(d)
vowel=["a","e","i","o","u"]
#to find the total number of vowels
n=int(input())
number=list(map(int,input().split(" ")))
c=0
for num in number:
    for char in d[num]:
        if char in vowel:
            c+=1
m=0
for i in range(n-1):
    for j in range(i+1,n):
        if number[i]+number[j]==c:
            m+=1
if m<=100:
    print(d[m],end="")
else:
    print("greater 100",end="")