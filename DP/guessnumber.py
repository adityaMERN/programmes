t=int(input())
for _ in range(t):
    n=int(input())
    l=[]
    for i in range(4*n-1):
        x=list(map(int,input().split(" ")))
        l.append(x)
    #print(l)
    d={}
    for j in l:
        f=[]
        if j[0] not in d:
            #create a list
            #f=[]
            d[j[0]]=f.append(j[1])
        else:
            f.append(j[1])
    print(d)

