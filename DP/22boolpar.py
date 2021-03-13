s=str(input())
n=len(s)
isTrue=True
def solve(s,i,j,isTrue):
    t=[[[-1 for a in range(2)]for b in range(len(s)+1)]for c in range(len(s)+1)]
    if i>j:
        return 0
    if i==j:
        if isTrue==True:
            return "T"==s[i]
        else:
            return "F"==s[i]
    #temp=""
    #temp=str(i)+" "
    #temp+=str(j)+" "
    #temp+=str(isTrue)
    if t[i][j][isTrue]!=-1:
        return t[i][j][isTrue]
    ans=0
    for k in range(i+1,j,2):
        #isTrue=True
        lT=solve(s,i,k-1,isTrue=True)
        #isTrue=False
        lF=solve(s,i,k-1,isTrue=False)
        #isTrue=True
        rT=solve(s,k+1,j,isTrue=True)
        #isTrue=False
        rF=solve(s,k+1,j,isTrue=False)
        if s[k]=="^":
                if isTrue:
                    ans=ans+(lT*rF)+(rT*lF)
                else:
                    ans=ans+(lT*rT)+(lF*rF)
        elif s[k]=="|":
                if isTrue:
                    ans=ans+(lF*rT)+(lT+rF)+(lT*rT)
                else:
                    ans=ans+(lF*rF)
        elif s[k]=="&":
                if isTrue:
                    ans=ans+(lT*rT)
                else:
                    ans=ans+(lF*rF)+(lF+rT)+(lT*rF)
    t[i][j][isTrue]=ans
    #print(t)
    return ans
x=solve(s,0,n-1,isTrue)
print(x)
