t=int(input())
n,q=map(int,input().split(" "))
a=list(map(int,input().split(" ")))
x=[]
for i in range(q):
    query=[]
    l,r=map(int,input().split(" "))
    query.append(l)
    query.append(r)
    x.append(query)
 