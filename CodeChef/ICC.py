# https://www.codechef.com/RTR2021/problems/ICC
def maxRepeating(s):
    n = len(s)
    maxcount = 1
    currcount=1
    maxChar=s[0]
    currChar=s[0]
    for i in range(1,n):
        if currChar==s[i]:
            currcount+=1
            if currcount>maxcount:
                maxcount=currcount
                maxChar=currChar
        else:
            currcount=1
            currChar=s[i]
    print(maxcount,maxChar)    
t=int(input())
for _ in range(t):
    s=str(input())
    maxRepeating(s)
    
