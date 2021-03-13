from itertools import product
low,h=map(int,input().split(" "))
k=int(input())
sum=0
l=[]
for i in range(low,h+1):
    l.append(str(i))
c=0
p=product(l,repeat=k)
#summ=0

for i in p:
    summ=0
    for j in range(len(i)):
        summ=summ+int(i[j])
    if summ%2==0:
        c+=1
print(c%1000000007)
        

