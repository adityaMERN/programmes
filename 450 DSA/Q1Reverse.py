#https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/
l=list(map(int,input().split(" ")))
#print(l[::-1])
n=len(l)

inital=0
final=n-1
for i in range(n//2):
    temp=l[i]
    b=l[n-1-i]
    l[i]=b
    l[n-1-i]=temp
print(l)

#We can use string slicing technique. 
#To use the logic, We will iterate from 0 to half length of the list then we will simple use the swaping the values of 
#two variables using a third variable.
#Time complexity: O(n)
#Space complexity: O(1)