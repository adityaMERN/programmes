n=int(input())
total=n*5
final=[]
for i in range(1,total+1,5):
    l=[]
    l.append(i)
    l.append(i+1)
    l.append(i+2)
    l.append(i+3)
    l.append(i+4)
    final.append(l)
for i in range(len(final)):
     if i%2!=0:
        final[i].reverse()

for i in range(n):
    print(*final[i])
    