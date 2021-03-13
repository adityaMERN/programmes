n=int(input())
l=[]
leads=[]
first=0
second=0
for i in range(n):
    p1,p2=map(int,input().split(" "))
    p1+=first
    p2+=second
    l.append([p1,p2])
    first=p1
    second=p2
#print(l)
for i in l:
    if i[0]>i[1]:
        leads.append([1,i[0]-i[1]])
    elif i[1]>i[0]:
        leads.append([2,i[1]-i[0]])
    
    
leads.sort(key=lambda x: int(x[1]),reverse=True)
#print(leads)
print(leads[0][0],leads[0][1])