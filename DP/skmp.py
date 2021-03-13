t=int(input())
for _ in range(t):
    s=str(input())
    p=str(input())
    stringS=list(s)
    stringS.sort()
    final=""
    #print(stringS)
    d={}
    for character in stringS:
        if character in d:
            d[character]+=1
        else:
            d[character]=1
    #print(d)
    for i in range(len(p)):
        x=p[i]
        d[x]-=1
    #print(d)
    #j=p[0]
    sortedkeys = sorted(d, key=str.lower)
    for keys in sortedkeys:
        if ord(p[0])==ord(keys):
            final+=p
            if d[keys]>0:
                final+=keys*d[keys]
            
        elif ord(p[0])>ord(keys):
            final+=keys*d[keys]
        else:
            final+=keys*d[keys]
    print(final)