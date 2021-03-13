import math
t=int(input())
for _ in range(t):
    n,x=map(int,input().split(" "))
    l=list(map(int,input().split(" ")))
    i=0
    o=0
    for g in range(x,0,-1):
        if i<n-1:
            w=0
            p=math.log(l[i])//math.log(2)
            print(p)
            r=2**int(p)
            #print(r)
            l[i]=l[i] ^ r
            for j in range(i+1,n):
                if l[j]^r<l[j]:
                    l[j]=l[j]^r
                    w=1
                    break
            if w==0:
                l[n-1]=l[n-1]^r
            while l[i]<=0:
                i+=1
                o=g+1
    if o>0:
        if n<3 and o%2>0:
            l[n-2]^=1
            l[n-1]^=1
    for i in range(n):
        print(l[i],end=" ")



