t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split(" ")))
    d=0
    fuel=l[0]
    for i in range(1,len(l)):
        if fuel==0:
            break
        fuel=fuel+l[i]-1
        d+=1
    print(d+fuel)
       
            
    




        