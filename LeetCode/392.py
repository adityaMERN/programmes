def isSubsequence(s, t):
        c=0
        if not s:
            return "POSITIVE"
        if not t:
            return "NEGATIVE"
        for j in t:
            if j==s[c]:
                c+=1
        #print(c)
            if len(s)==c:
                return "POSITIVE" 
        return "NEGATIVE"
t=str(input())
n=int(input())
for _ in range(n):
    s=str(input())
    x=isSubsequence(s,t)
    print(x)