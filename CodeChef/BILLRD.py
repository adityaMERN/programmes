#january long challenge codechef 4th question

t=int(input())
for _ in range(t):
    n,k,x,y=map(int,input().split(" "))
    l=[]
    if x==y:
        print(n,n)
    elif x>y:
        point1=[n,y+n-x]
        point2=[y+n-x,n]
        point3=[0,x-y]
        point4=[x-y,0]
        l.append(point1)
        l.append(point2)
        l.append(point3)
        l.append(point4)
        #print(l)
        point=(k-1)%4
        print(l[point][0],l[point][1])
    elif x<y:
        point1=[x+n-y,n]
        point2=[n,x+n-y]
        point3=[y-x,0]
        point4=[0,y-x]
        l.append(point1)
        l.append(point2)
        l.append(point3)
        l.append(point4)
        #print(l)
        point=(k-1)%4
        print(l[point][0],l[point][1])
    