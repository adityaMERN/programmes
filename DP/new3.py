
def solution(s):
    i=0
    j=len(s)-1
    l=[* for i in range(len(s))]
    while i<=j:
        if s[i]=="?" and s[j]!="?":
            l[i]=s[j]
            i+=1
            j-=1
        elif s[i]!="?" and s[j]=="?":
            l[j]=s[i]
            i+=1
            j-=1
        
        else:
            if s[i]==s[j]:
                i+=1
                j-=1
                l[i]=z        
            else:
                break
    x="".join(l)
    if x==s:
        return x
    else:
        return "NO"
