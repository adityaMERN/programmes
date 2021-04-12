# def convert(integer):
#     binary=bin(integer).replace("0b", "")
#     return binary
# def isSubSequence(str1, str2):
#     m = len(str1)
#     n = len(str2)
#     j = 0    
#     i = 0    
#     while j < m and i < n:
#         if str1[j] == str2[i]:
#             j = j+1
#         i = i + 1
#     return j == m
# t=int(input())
# for _ in range(t):
#     string1=str(input())
#     flag=0
#     for each in string1:
#         if each=="0":
#             flag=1
#     if flag=="0":
#         print("0")
#     else:
#         intege=int(string1,2)
#         #print(intege)
#         for i in range(intege+1):
#             string2=convert(i)
#             #print(string2)
#             if isSubSequence(string2, string1):
#                 continue
#             else:
#                 print(string2)
#                 break 
maxn=10**6
dp=[0 for i in range(maxn+2)]
dp1=[0 for i in range(maxn+2)]
next0=[0 for i in range(maxn)]
next1=[0 for i in range(maxn)]
def function():
    s=str(input())
    n=len(s)
    lastPosition=-1
    for i in range(n):
        if s[i]=="0":
            for j in range(lastPosition+1,i+1):
                next0[j]=i
            lastPosition=i
    for i in range(lastPosition+1,n):
        next0[i]=n
    if next0[0]==n:
        return 0
    lastPosition=-1
    for i in range(0,n):
        if s[i]=="1":
            for j in range(lastPosition+1,i+1):
                next1[j]=i
            lastPosition=i
    for i in range(lastPosition+1,n):
        next1[i]=n
    dp[n]=dp[n+1]=0
    dp1[n]=dp1[n+1]=0
    for i  in range(n-1,-1,-1):
        dp[i]=dp[i+1]
        if s[i]=="0" and next1[i]<n:
            dp[i]=max(dp[i],dp[next1[i]+1]+1)
        if s[i]=="1"and next0[i]<n:
            dp[i]=max(dp[i],dp[next0[i]+1]+1)
        dp1[i]=dp1[i+1]
        if (next1[i]<n):
            dp1[i]=max(dp1[i],dp[next1[i]+1]+1)
    length=dp1[0]+1
    c=next1[0]+1
    ans="1"
    for i in range(1,length):
        if c>=n:
            ans+="0"
            continue
        if next0[c]>=n:
            ans+="0"
            c=next0[c]+1
            continue
        if dp[next0[c]+1]<length-i-1:
            ans+="0"
            c=next0[c]+1
        else:
            ans+="1"
            c=next1[c]+1
    return ans
t=int(input())
for _ in range(t):
    output=function()
    print(output)
    
    
