t=int(input())
for _ in range(t):
    n= int(input())
    arr=list(map(int,input().split(" ")))
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    sort_orders = sorted(d.items(), key=lambda x: x[1])
    #print(sort_orders)
    x=[]
    for i in sort_orders:
        x.append(i[1])
    new_d={}

    for k in x:
        if k in new_d:
            new_d[k]+=1
        else:
            new_d[k]=1
    #print(new_d)
    #l=[]
    for item in new_d:
        l=[[k,v] for k ,v in new_d.items()]
    #print(l)
    z=[]
    for i in range(len(l)):
        z.append(l[i][1])
    #print(z)
    #print()
    xx=z.count(z[0])
    #print(xx)
    if xx==len(z):
        l.sort(key = lambda x: x[0])
        #print(l)
        print(l[0][0])
    else:
        l.sort(key = lambda x: x[1],reverse=True)
        #print(l)
        print(l[0][0])

    #sort_ordersnew = sorted(new_d.items(), key=lambda x: x[0])
    #print(sort_ordersnew)
    #print()
    #for i in sort_ordersnew:
        #if sort_ordersnew.count(i[1])==len(sort_ordersnew):
            #print(sort_ordersnew[0][0])
        #else:


