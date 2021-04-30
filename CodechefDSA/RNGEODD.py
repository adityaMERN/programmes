l,r=map(int,input().split(" "))
il=[]
for i in range(l,r+1):
    if i%2!=0:
        il.append(i)
print(*il)
