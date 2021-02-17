#question link: https://www.codechef.com/FEB21C/problems/SUMXOR2
import math
 
def printSubsequences(arr, n) :
    opsize = math.pow(2, n)
    x=[]
    for counter in range( 1, (int)(opsize)) :
        l=[]
        for j in range(0, n) :
            if (counter & (1<<j)) :
                l.append(arr[j])
                #print( arr[j], end =" ")
        x.append(l)
    
         
    return x
n=int(input())
l=list(map(int,input().split(" ")))
# binary=[]
# for each in l:
#     x= bin(each).replace("0b", "")
#     length=len(x)
#     count=32-length
#     binary.append(("0"*count+x))
#     print(binary)
dp=[0 for i in range(1000)]
dp[0]=sum(l)

q=int(input())
querylist=[]
for _ in range(q):
    m=int(input())
    querylist.append(m)
mx=max(querylist)
for each in querylist:
    

        

            

    