#january long challenge codechef 7th question

t=int(input())
for _ in range(t):
    n,m=map(int,input().split(" "))
    A=list(map(int,input().split(" ")))
    B=list(map(int,input().split(" ")))
    s={}
    for i in range(n):
        stack=[]
        stack.push(0)
        while len(stack)!=0:
            x=stack[-1]
            stack.pop()
            for k in range(n):
                y=A[k]
                if x|y in s
    for i in range(m):
        l=[]
        for k in s:
            l.append(k)
        x=l[-1]&B[i]
        if x not in s:
            s.add(x)
    
    #print(s)
    print(len(s))




    
