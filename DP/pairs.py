n=int(input())
l=list(map(int,input().split(" ")))
new=[]
for i in range(n):
    #print(l[i])
    x=list(str(l[i]))
    x.sort()
    #print(x)
    value=(7*int(x[0]))+(11*int(x[2]))
    new.append(value)
#print(new)
odd=[]
even=[]
for i in range(len(new)):
    sig=str(new[i])[0]
    if i%2!=0:
        odd.append(sig)
    else:
        even.append(sig)
#print(odd)
#print(even)
d={}
for a in odd:
    if a in d:
        d[a]+=1
    else:
        d[a]=1
#print(d)

de={}
for b in even:
    if b in de:
        de[b]+=1
    else:
        de[b]=1
#print(de)
countodd=0
counteven=0
used=[]
for key in d:
    if key not in used and d[key]>2:
        countodd+=2
        used.append(key)

    elif key not in used and d[key]==2:
        countodd+=1
        used.append(key)

for key in de:
    if key not in used and de[key]>2 :
        counteven+=2
        used.append(key)
    elif key not in used and de[key]==2:
        counteven+=1
        used.append(key)
print(used)
print(countodd+counteven)

