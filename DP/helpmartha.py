def subSequence(string,s):
            m=len(string)
            n=len(s)
            i=0
            j=0
            while j<m and i<n:
                if string[j]==s[i]:
                    j+=1
                i+=1
            return j==m
t=int(input())
for _ in range(t):
    s=str(input())
    x1,y1=map(int,input().split(" "))
    q=int(input())
    #l=[]
    for i in range(q):
        x,y=map(int,input().split(" "))
        string=""
        if x>x1:
            string+="R"*(x-x1)
        if x<x1:
            string+="L"*(x1-x)
        if y>y1:
            string+="U"*(y-y1)
        if y<y1:
            string+="D"*(y1-y)
        print(string)
        if subSequence(string,s):
            print("YES"+" "+str(len(string)))
        else:
            print("NO")

