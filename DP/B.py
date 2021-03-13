n,d=map(int,input().split(" "))
c=0
for i in range(n):
    x,y=map(int,input().split(" "))
    distance=((x-0)**2+(y-0)**2)**(0.5)
    if distance<=d:
        c+=1
print(c)